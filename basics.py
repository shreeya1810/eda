from load_data import load_data
import seaborn as sns

# Load dataset
data = sns.load_dataset("iris")

# Data types and summary
print("Data Types:\n", data.dtypes)
print("\nSummary Statistics:\n", data.describe(include='all'))
