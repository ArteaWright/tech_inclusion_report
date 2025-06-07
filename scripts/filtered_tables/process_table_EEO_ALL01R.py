import pandas as pd

eeo_all01r_path = "data\EEO-ALL01R_US_2014-2018.xlsx"
role_mapping_path = "outputs/role_mapping_output.xlsx"


# Load and display the 'Data' sheet
df_all01r = pd.read_excel(eeo_all01r_path , sheet_name="Data")

# Step 1: Skip top non-data rows again, starting from where actual occupations begin
df_all01r_cleaned = pd.read_excel(eeo_all01r_path , sheet_name="Data", skiprows=2)

# Step 2: Rename columns meaningfully
df_all01r_cleaned.columns = [
    "Occupation",
    "Gender",
    "Total_All",
    "Hispanic_or_Latino",
    "White_Alone",
    "Black_Alone",
    "Native_American_Alone",
    "Asian_Alone",
    "Pacific_Islander_Alone",
    "Balance_Not_Hispanic"
]


# Drop rows with missing occupation data
df_all01r_cleaned.dropna(subset=["Occupation"], inplace=True) 

# Filter to keep only rows where Gender is 'Total'
df_filtered = df_all01r_cleaned[df_all01r_cleaned["Gender"] == "Percent Total"].copy()

# Redefine the alias mapping provided by the user for EEO occupation matching
soc_to_eeo = {
    "Data Scientist": "Mathematical science occupations : 15-2000 / 1200",
    "Management Analyst": "Management analysts : 13-1111 / 0710",
    "Database Architects": "Database and network administrators and architects : 15-1240 / 1065",
    "Software Developer": "Software and web developers, programmers, and testers : 15-1250 / 1010",
    "Information Security Analysts": "Computer and information research scientists and analysts : 15-12XX / 1005",
    "Computer System Analyst": "Computer and information research scientists and analysts : 15-12XX / 1005",
    "Aerospace Engineers": "Aerospace engineers : 17-2011 / 1320",
    "Engineers, All Other": "Other engineers : 17-21YY / 1530",
    "Statisticians": "Mathematical science occupations : 15-2000 / 1200",
    "Medical Scientists, Except Epidemiologists": "Other life scientists : 19-10XX / 1650",
    "Environmental Scientists and Specialists": "Environmental scientists and geoscientists : 19-2040 / 1745",
    "Computer Hardware Engineers": "Computer hardware engineers : 17-2061 / 1400",
    "Graphic Designers": "Art and design workers : 27-1000 / 2600",
    "Electronics Engineers, Except Computer": "Electrical and electronics engineers : 17-2070 / 1410"
}

# Create a list of unique EEO occupations based on the mapping
relevant_eeo_occupations = list(set(soc_to_eeo.values()))

# Filter the previously cleaned df_filtered to keep only relevant occupations
df_eeo_filtered = df_filtered[df_filtered["Occupation"].isin(relevant_eeo_occupations)].copy()

# Clean occupation column for consistency
df_eeo_filtered["Occupation_clean"] = df_eeo_filtered["Occupation"].str.lower().str.strip()

# Convert percentage columns to proportions if needed
percent_columns_eeo01 = [col for col in df_eeo_filtered.columns if any(x in col.lower() for x in ["white", "black", "asian", "hispanic", "women", "men"])]
for col in percent_columns_eeo01:
    df_eeo_filtered[col] = pd.to_numeric(df_eeo_filtered[col], errors="coerce") * 100


# Save the updated filtered data
final_output_path = "outputs/eeo_all01r_filtered.xlsx"
df_eeo_filtered.to_excel(final_output_path, index=False)

final_output_path
