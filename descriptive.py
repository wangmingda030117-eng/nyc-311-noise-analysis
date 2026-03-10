import pandas as pd
import matplotlib.pyplot as plt

# 1. Path to cleaned dataset
clean_path = r"C:\Users\wmdgod\Desktop\Data\Final\output\cleaned_311_noise_2025.csv"

print("Loading cleaned data...")
df = pd.read_csv(clean_path)
print("Rows in cleaned data:", len(df))

# 2. Count complaints by borough
borough_counts = df["Borough"].value_counts().sort_values(ascending=False)
print("Counts by borough:")
print(borough_counts)

# 3. Plot bar chart of complaints by borough
plt.figure(figsize=(8, 5))
borough_counts.plot(kind="bar")

plt.title("Noise Complaints by Borough (2025)")
plt.xlabel("Borough")
plt.ylabel("Number of complaints")
plt.tight_layout()

# 4. Save the figure
plot_path = r"C:\Users\wmdgod\Desktop\Data\Final\output\borough_counts.png"
plt.savefig(plot_path, dpi=300)

print("Bar chart saved to:", plot_path)
plt.close()
