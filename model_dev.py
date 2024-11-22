from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

model = LinearRegression().fit(X, y)
y_pred = model.predict(X)
print("Mean Squared Error:", mean_squared_error(y, y_pred))
