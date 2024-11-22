from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Data
data = [[1, 2], [3, 4], [5, 6], [7, 8]]

# Hierarchical clustering
linked = linkage(data, method='ward')

# Dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked)
plt.title("Dendrogram")
plt.show()
