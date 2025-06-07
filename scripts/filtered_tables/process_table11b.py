import pandas as pd

# Load the file 
table_11b_path = "data/cpsaat11b.xlsx"
role_mapping_path = "outputs/role_mapping_output.xlsx"

# Step 1: Load the file again with appropriate parsing (if needed)
df_11b = pd.read_excel(table_11b_path, sheet_name="cpsaat11b", skiprows=6)

# Step 2: Rename columns to meaningful names for age groups
df_11b.columns = [
    "Occupation", "Total Employed", "Age 16-19", "Age 20-24", "Age 25-34",
    "Age 35-44", "Age 45-54", "Age 55-64", "Age 65+", "Median Age"
]

# Step 3: Drop empty rows
df_11b.dropna(subset=["Occupation"], inplace=True)

# Step 4: Normalize occupation titles
df_11b["Occupation_normalized"] = df_11b["Occupation"].str.lower().str.strip()

# Step 5: Apply same normalization and alias logic
role_df = pd.read_excel(role_mapping_path)
role_df["SOC Code Description Normalized"] = role_df["SOC Code Description"].str.lower().str.strip()

# Define aliases for known BLS occupation naming differences
normalized_aliases = {
    "data scientists": "database administrators and architects",
    "database architects": "database administrators and architects",
    "electronics engineers, except computer": "electrical and electronics engineers",
    "environmental scientists and specialists": "environmental scientists and specialists, including health",
    "medical scientists, except epidemiologists": "medical scientists"
}

# Apply alias replacements
normalized_occupations = role_df["SOC Code Description Normalized"].dropna().tolist()
normalized_occupations_with_aliases = [normalized_aliases.get(role, role) for role in normalized_occupations]

# Step 6: Filter the table for matching occupations
filtered_df_11b = df_11b[df_11b["Occupation_normalized"].isin(normalized_occupations_with_aliases)]

# Step 7: Save output to verify results
output_path_11b = "outputs/table_11b_filtered_age_distribution.xlsx"
filtered_df_11b.to_excel(output_path_11b, index=False)

output_path_11b
