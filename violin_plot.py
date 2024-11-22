import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {'A': [10, 12, 13, 14, 15], 'B': [5, 6, 7, 8, 9]}
sns.violinplot(data=pd.DataFrame(data))
plt.title("Violin Plot")
plt.show()
