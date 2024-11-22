from sklearn.decomposition import PCA
import numpy as np

# Data
data = np.random.rand(10, 5)

# PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data)
print("Reduced Data:\n", reduced_data)
