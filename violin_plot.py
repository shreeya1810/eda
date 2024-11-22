from load_data import load_data
data = load_data()
sns.violinplot(x='species', y='petal_length', data=data)
plt.title("Violin Plot: Petal Length by Species")
plt.show()
