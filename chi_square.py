from scipy.stats import chi2_contingency

# Example Data
data = pd.DataFrame({
    "Gender": ["Male", "Male", "Female", "Female", "Female"],
    "Likes_Sports": ["Yes", "No", "Yes", "Yes", "No"]
})

# Contingency Table
contingency_table = pd.crosstab(data["Gender"], data["Likes_Sports"])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-Square Statistic: {chi2}, p-value: {p}")
