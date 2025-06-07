import pandas as pd 

file_path_04r = "data\EEO-ALL04R_US_2014-2018.xlsx"

# Load the "Data" sheet
df_04r_raw = pd.read_excel(file_path_04r, sheet_name="Data")

# === Step 2: Skip metadata rows and load the data cleanly ===
df_04r = pd.read_excel(file_path_04r, sheet_name="Data", skiprows=2)

# === Step 3: Rename columns clearly ===
df_04r.columns = [
    "Occupation", "Sex", "Total", "Hispanic or Latino", "White",
    "Black or African American", "American Indian/Alaska Native", "Asian",
    "Native Hawaiian/Pacific Islander", "Balance of Not Hispanic or Latino"
]

# === Step 4: Keep only 'Total' rows for each job category ===
df_04r_filtered = df_04r[df_04r["Sex"] == "Percent Total"].copy()

# Clean occupation column for consistency
df_04r_filtered["Occupation_clean"] = df_04r_filtered["Occupation"].str.lower().str.strip()

# Convert percentage-based demographic columns to proportions
percent_columns_eeo04 = [col for col in df_04r_filtered.columns if any(x in col.lower() for x in ["white", "black", "asian", "hispanic", "women", "men"])]
for col in percent_columns_eeo04:
    df_04r_filtered[col] = pd.to_numeric(df_04r_filtered[col], errors="coerce") * 100

# Save the updated filtered data
final_output_path = "outputs/eeo_all04r_filtered.xlsx"
df_04r_filtered.to_excel(final_output_path, index=False)

final_output_path


