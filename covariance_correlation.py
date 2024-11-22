from load_data import load_data
# Covariance
data = load_data()
print("Covariance Matrix:\n", data[['sepal_length', 'sepal_width']].cov())

# Correlation
print("Correlation Matrix:\n", data[['sepal_length', 'sepal_width']].corr())
