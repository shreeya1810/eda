import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {'A': [10, 20, 30, 100, 40], 'B': [5, 15, 25, 50, 10]}
sns.boxplot(data=list(data.values()))
plt.title("Boxplot for Outlier Detection")
plt.xlabel("Features")
plt.ylabel("Values")
plt.show()
