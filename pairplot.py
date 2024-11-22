from load_data import load_data
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")

# Pairplot
sns.pairplot(df, hue="species")
plt.show()
