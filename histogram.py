from load_data import load_data
data = load_data()
sns.histplot(data['petal_length'], bins=10, kde=True)
plt.title("Histogram: Petal Length Distribution")
plt.show()
