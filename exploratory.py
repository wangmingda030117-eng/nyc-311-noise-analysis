import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
clean_path = r"C:\Users\wmdgod\Desktop\Data\Final\output\cleaned_311_noise_2025.csv"
df = pd.read_csv(clean_path)
top5 = df["Descriptor"].value_counts().nlargest(5).index 
df["Descriptor"] = df["Descriptor"].where(df["Descriptor"].isin(top5), "Other")
# Group by Borough and Descriptor
pivot = df.groupby(["Borough", "Descriptor"]).size().unstack(fill_value=0)

print("Borough × Descriptor table:")
print(pivot)

# Plot stacked bar chart
plt.figure(figsize=(12, 6))
pivot.plot(kind="bar", stacked=True, colormap="tab20", figsize=(12, 6))

plt.title("Noise Complaint Descriptors by Borough (2025)")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.tight_layout()

plot_path = r"C:\Users\wmdgod\Desktop\Data\Final\output\borough_descriptor.png"
plt.savefig(plot_path, dpi=300)
plt.close()

print("Saved figure to:", plot_path)
