from load_data import load_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data = load_data()
# Data preparation
X = data[['sepal_length', 'sepal_width']]
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Logistic Regression Accuracy:", accuracy)
