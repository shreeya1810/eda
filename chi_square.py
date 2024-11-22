from load_data import load_data
from scipy.stats import chi2_contingency
data = load_data()
# Create a contingency table
contingency_table = pd.crosstab(data['species'], data['sepal_length_binned'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print("Chi-square Test:\nChi2:", chi2, "p-value:", p)
