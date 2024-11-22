import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Input data
data = np.array([10, 20, 30, 40, 50])

# Scale data to [0, 1]
scaler_01 = MinMaxScaler(feature_range=(0, 1))
scaled_01 = scaler_01.fit_transform(data.reshape(-1, 1))
print("Scaled [0, 1]:", scaled_01.flatten())

# Scale data to [-1, 1]
scaler_11 = MinMaxScaler(feature_range=(-1, 1))
scaled_11 = scaler_11.fit_transform(data.reshape(-1, 1))
print("Scaled [-1, 1]:", scaled_11.flatten())

# Scale data to [-3, 3]
scaler_33 = MinMaxScaler(feature_range=(-3, 3))
scaled_33 = scaler_33.fit_transform(data.reshape(-1, 1))
print("Scaled [-3, 3]:", scaled_33.flatten())
