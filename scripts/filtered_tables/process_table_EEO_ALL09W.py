import pandas as pd 

file_path_09w = "data\EEO-ALL09W_US_2014-2018.xlsx"
df_01r_filtered = pd.read_excel("outputs/eeo_all01r_filtered.xlsx")

# === Step 1: Skip the top metadata rows and load relevant data cleanly ===
df_09w = pd.read_excel(file_path_09w, sheet_name="Data", skiprows=2)

# Standardize column names
df_09w.columns = [
    "Occupation", "Industry", "Total", "Hispanic or Latino", "White",
    "Black or African American", "American Indian/Alaska Native", "Asian",
    "Native Hawaiian/Pacific Islander", "Balance of Not Hispanic or Latino"
]

# Re-filter the data keeping only rows where Industry is "Total"
df_09w_industry_total = df_09w[df_09w["Industry"] == "Percent Total"].copy()

# Further filtering by SOC 

# Helper function to extract the SOC code portion from occupation strings
def extract_soc_code(text):
    if isinstance(text, str) and ":" in text:
        try:
            return text.split(":")[1].strip().split(" ")[0]  # Get "13-1111" from "Management analysts: 13-1111 / 0710"
        except IndexError:
            return None
    return None

# Extract SOC codes from both datasets
df_09w_industry_total["SOC Code"] = df_09w_industry_total["Occupation"].apply(extract_soc_code)
df_01r_filtered["SOC Code"] = df_01r_filtered["Occupation"].apply(extract_soc_code)

# Filter EEO-ALL09W for SOC codes found in the EEO-ALL01R filtered data
valid_soc_codes = df_01r_filtered["SOC Code"].dropna().unique()
df_09w_final_filtered_by_soc = df_09w_industry_total[df_09w_industry_total["SOC Code"].isin(valid_soc_codes)].copy()

# Drop helper column before saving if needed
df_09w_final_filtered_by_soc.drop(columns=["SOC Code"], inplace=True)

# Clean and standardize the Occupation column
df_09w_final_filtered_by_soc["Occupation_clean"] = df_09w_final_filtered_by_soc["Occupation"].str.lower().str.strip()

# Convert selected demographic columns to proportions (if they are not already in counts)
percent_columns_eeo09 = [
    "White", "Black or African American", "Asian", "Hispanic or Latino"
]
for col in percent_columns_eeo09:
    df_09w_final_filtered_by_soc[col] = pd.to_numeric(df_09w_final_filtered_by_soc[col], errors="coerce") * 100


# Save this intermediate result for inspection
intermediate_output_path_09w = "outputs/eeo_all09w_industry_total.xlsx"
df_09w_final_filtered_by_soc.to_excel(intermediate_output_path_09w, index=False)

