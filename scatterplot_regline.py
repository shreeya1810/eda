import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 5, 4, 5]}
sns.regplot(x='X', y='Y', data=pd.DataFrame(data))
plt.title("Scatterplot with Regression Line")
plt.show()
