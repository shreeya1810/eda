from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Input data
X = [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7]]
y = [0, 0, 0, 1, 1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# K-Nearest Neighbor classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Results
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
