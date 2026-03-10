import pandas as pd
import numpy as np

# 1. Load cleaned data
clean_path = r"C:\Users\wmdgod\Desktop\Data\Final\output\cleaned_311_noise_2025.csv"
df = pd.read_csv(clean_path)

# 2. Count complaints by borough
borough_counts = df["Borough"].value_counts().sort_index()
print("Observed counts by borough:")
print(borough_counts)

# 3. Build expected counts under H0 (evenly distributed)
k = len(borough_counts)              # number of boroughs
total = borough_counts.sum()         # total complaints
expected = np.repeat(total / k, k)   # equal share for each borough

print("\nExpected counts under H0 (even distribution):")
print(expected)

# 4. Chi-square statistic (manual calculation)
chi2 = (((borough_counts.values - expected) ** 2) / expected).sum()
dfree = k - 1                        # degrees of freedom

print("\nChi-square statistic:", chi2)
print("Degrees of freedom:", dfree)

# 5. Decision using critical value at alpha = 0.05
# For df = 4 (5 boroughs), chi-square critical ≈ 9.49
critical_value = 9.49

if chi2 > critical_value:
    print("\nResult: chi2 > 9.49 -> reject H0.")
    print("Conclusion: Noise complaint volume is NOT evenly distributed across boroughs.")
else:
    print("\nResult: chi2 <= 9.49 -> fail to reject H0.")
    print("Conclusion: We do NOT have enough evidence to say the distribution is uneven.")
