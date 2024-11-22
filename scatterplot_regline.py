from load_data import load_data
data = load_data()
sns.regplot(x='sepal_length', y='sepal_width', data=data)
plt.title("Scatterplot with Regression Line")
plt.show()
