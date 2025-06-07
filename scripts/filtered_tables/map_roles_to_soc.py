import pandas as pd

# === Define Your Emerging Tech Roles ===
emerging_tech_roles = [
    "AI/Machine Learning Engineer",
    "AI Ethics & Compliance Specialist",
    "Natural Language Processing (NLP) Engineer",
    "AI Solutions Architect",
    "Blockchain Developer",
    "Smart Contract Developer",
    "Blockchain Security Specialist",
    "Blockchain Analyst/Consultant",
    "Computer Vision Engineer",
    "Autonomous Vehicle Software Engineer",
    "AeroSpace Engineer",
    "Robotics Engineer",
    "Sensor Fusion Engineer",
    "Bioinformatics Specialist",
    "Biomedical Data Scientist",
    "Genomics Engineer",
    "AI Healthcare Solutions Engineer",
    "Climate Data Analyst",
    "Renewable Energy Systems Engineer",
    "Sustainability Tech Specialist",
    "AgTech IoT Engineer",
    "AR/VR Developer",
    "Spatial Computing Designer",
    "XR (Extended Reality) Engineer",
    "AR/VR Experience Designer", 
    "Quantum Computing Engineer",
    "Quantum Algorithm Developer",
    "Quantum Hardware Engineer",
    "Quantum Information Scientist",
    "Quantum Software Engineer",
    "Quantum Systems Architect",
    "Quantum Cryptography Specialist"
]

# === Create an Empty DataFrame for Mapping ===
df = pd.DataFrame(emerging_tech_roles, columns=["Emerging Tech Role"])
df["Likely SOC Code"] = ""
df["SOC Code Description"] = ""
df["Notes"] = ""

soc_mappings = {
    "AI/Machine Learning Engineer": ("15-2051", "Data Scientists"),
    "AI Ethics & Compliance Specialist": ("13-1111", "Management Analysts"),
    "Natural Language Processing (NLP) Engineer": ("15-2051", "Data Scientists"),
    "AI Solutions Architect": ("15-1243", "Database Architects"),
    "Blockchain Developer": ("15-1252", "Software Developers"),
    "Smart Contract Developer": ("15-1252", "Software Developers"),
    "Blockchain Security Specialist": ("15-1212", "Information Security Analysts"),
    "Blockchain Analyst/Consultant": ("15-1241", "Computer Systems Analysts"),
    "Computer Vision Engineer": ("15-2051", "Data Scientists"),
    "Autonomous Vehicle Software Engineer": ("15-1252", "Software Developers"),
    "AeroSpace Engineer": ("17-2011", "Aerospace Engineers"),
    "Robotics Engineer": ("17-2199", "Engineers, All Other"),  # Often falls here or under Mechatronics
    "Sensor Fusion Engineer": ("15-2041", "Statisticians"),  # Close fit, or sometimes Systems Engineers (17-2112)
    "Bioinformatics Specialist": ("15-2051", "Data Scientists"),
    "Biomedical Data Scientist": ("15-2051", "Data Scientists"),
    "Genomics Engineer": ("19-1042", "Medical Scientists, Except Epidemiologists"),
    "AI Healthcare Solutions Engineer": ("15-2051", "Data Scientists"),
    "Climate Data Analyst": ("19-2041", "Environmental Scientists and Specialists"),
    "Renewable Energy Systems Engineer": ("17-2199", "Engineers, All Other"),
    "Sustainability Tech Specialist": ("19-2041", "Environmental Scientists and Specialists"),
    "AgTech IoT Engineer": ("17-2061", "Computer Hardware Engineers"),
    "AR/VR Developer": ("15-1252", "Software Developers"),
    "Spatial Computing Designer": ("27-1024", "Graphic Designers"),  # Approximate; for interface design
    "XR (Extended Reality) Engineer": ("15-1252", "Software Developers"),
    "AR/VR Experience Designer": ("27-1024", "Graphic Designers"), 
     "Quantum Computing Engineer": ("17-2199", "Engineers, All Other"),
    "Quantum Algorithm Developer": ("15-2051", "Data Scientists"),
    "Quantum Hardware Engineer": ("17-2072", "Electronics Engineers, Except Computer"),
    "Quantum Information Scientist": ("15-2041", "Statisticians"),
    "Quantum Software Engineer": ("15-1252", "Software Developers"),
    "Quantum Systems Architect": ("15-1243", "Database Architects"),
    "Quantum Cryptography Specialist": ("15-1212", "Information Security Analysts")
}

for index, row in df.iterrows():
    role = row["Emerging Tech Role"]
    if role in soc_mappings:
        soc_code, soc_desc = soc_mappings[role]
        df.at[index, "Likely SOC Code"] = soc_code
        df.at[index, "SOC Code Description"] = soc_desc

# === Preview the Table ===
print("\nEmerging Tech Role Mapping Table Preview:")
print(df.head(len(emerging_tech_roles)))

# === Save as Excel File in 'outputs' Folder ===
output_path = "outputs/role_mapping_output.xlsx"
df.to_excel(output_path, index=False)
print(f"\n✅ Mapping table saved to: {output_path}")
