import pandas as pd

# === Step 1: Define file paths ===
role_mapping_path = "outputs/role_mapping_output.xlsx"
table_11_path = "data/cpsaat11.xlsx"

# === Step 2: Load role mapping file and extract SOC Code Descriptions ===
role_df = pd.read_excel(role_mapping_path)
relevant_occupations = role_df["SOC Code Description"].dropna().unique().tolist()

# === Step 3: Load BLS Table 11 and clean ===
df_11 = pd.read_excel(table_11_path, sheet_name="cpsaat11", skiprows=6)
df_11.columns = [
    "Occupation",
    "Total Employed",
    "Percent Women",
    "Percent White",
    "Percent Black",
    "Percent Asian",
    "Percent Hispanic"
]
df_11.dropna(subset=["Occupation"], inplace=True)

# Define alias mapping for unmatched occupations to match BLS naming conventions
normalized_aliases = {
    "data scientists": "database administrators and architects",
    "database architects": "database administrators and architects",
    "electronics engineers, except computer": "electrical and electronics engineers",
    "environmental scientists and specialists": "environmental scientists and specialists, including health",
    "medical scientists, except epidemiologists": "medical scientists"
}

# Normalize BLS Occupation titles
df_11["Occupation_normalized"] = df_11["Occupation"].str.lower().str.strip()

# Normalize role-mapped SOC descriptions
role_df["SOC Code Description Normalized"] = role_df["SOC Code Description"].str.lower().str.strip()
normalized_occupations = role_df["SOC Code Description Normalized"].dropna().tolist()

# Apply alias replacements where needed
normalized_occupations_with_aliases = [normalized_aliases.get(role, role) for role in normalized_occupations]

# Final filter using the alias-adjusted and normalized occupation titles
filtered_df_final = df_11[df_11["Occupation_normalized"].isin(normalized_occupations_with_aliases)]

# Save the updated filtered data
final_output_path = "outputs/table_11_filtered.xlsx"
filtered_df_final.to_excel(final_output_path, index=False)

final_output_path
