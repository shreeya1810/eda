import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Correlation matrix
data = {'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1], 'C': [10, 20, 30, 40]}
df = pd.DataFrame(data)
corr = df.corr()

# Heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
