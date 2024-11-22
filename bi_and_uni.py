from load_data import load_data
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = load_data()

# Univariate Analysis
sns.histplot(data['sepal_length'], kde=True, bins=10)
plt.title("Univariate Analysis: Sepal Length Distribution")
plt.show()

# Bivariate Analysis
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data)
plt.title("Bivariate Analysis: Sepal Length vs Sepal Width")
plt.show()
