from load_data import load_data
data = load_data()
sns.boxplot(x='species', y='sepal_length', data=data)
plt.title("Boxplot: Sepal Length by Species")
plt.show()
