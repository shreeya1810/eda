from sklearn.ensemble import RandomForestClassifier

# Data
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 1, 0, 1]

# Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X, y)
print("Predicted:", rf.predict([[4, 5]]))
