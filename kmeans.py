from load_data import load_data
from sklearn.cluster import KMeans
data = load_data()
kmeans = KMeans(n_clusters=3, random_state=42)
data['kmeans_cluster'] = kmeans.fit_predict(data[['sepal_length', 'sepal_width']])
print("Cluster Centers:\n", kmeans.cluster_centers_)
