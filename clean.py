import pandas as pd

# 1. Path to the raw dataset
raw_path = r"C:\Users\wmdgod\Desktop\Data\Final\Data\311_Service_Requests_from_2010_to_Present_20251204.csv"

# 2. Read only necessary columns
use_cols = [
    "Created Date",
    "Complaint Type",
    "Descriptor",
    "Borough",
    "Latitude",
    "Longitude"
]

print("Loading raw CSV...")
df = pd.read_csv(raw_path, usecols=use_cols, low_memory=False)
print("Rows in raw data:", len(df))

# 3. Filter noise-related complaints
df = df[df["Complaint Type"].str.contains("Noise", na=False)]
print("Rows after filtering noise complaints:", len(df))

# 4. Convert Created Date to datetime
df["Created Date"] = pd.to_datetime(df["Created Date"], errors="coerce")
df = df.dropna(subset=["Created Date"])

# Keep only records from 2025 onward
df = df[df["Created Date"] >= "2025-01-01"]
print("Rows after filtering date >= 2025:", len(df))

# 5. Drop missing borough or coordinates
df = df.dropna(subset=["Borough"])
# Drop rows where Borough is explicitly 'Unspecified' or empty string
df = df[df["Borough"].str.upper() != "UNSPECIFIED"]
df = df[df["Borough"].str.strip() != ""]
# Drop rows missing coordinates
df = df.dropna(subset=["Latitude", "Longitude"])
print("Rows after dropping missing borough/coordinates:", len(df))

# 6. Save the cleaned dataset
clean_path = r"C:\Users\wmdgod\Desktop\Data\Final\output\cleaned_311_noise_2025.csv"
df.to_csv(clean_path, index=False)

print("Cleaning completed.")
print("Final row count:", len(df))
print("Saved to:", clean_path)
print(df.head())
