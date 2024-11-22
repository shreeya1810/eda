from load_data import load_data
from scipy.cluster.hierarchy import dendrogram, linkage
data = load_data()
Z = linkage(data[['sepal_length', 'sepal_width']], method='ward')
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()
