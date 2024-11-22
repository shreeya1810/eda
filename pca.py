from load_data import load_data
from sklearn.decomposition import PCA
data = load_data()
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
print("PCA Reduced Data:\n", reduced_data[:5])
