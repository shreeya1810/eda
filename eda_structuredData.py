import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('iris')

# Summary statistics
print(df.describe())

# Pairplot for feature relationships
sns.pairplot(df, hue='species')
plt.show()

# Boxplot to check for outliers
sns.boxplot(data=df.drop(columns='species'))
plt.show()
