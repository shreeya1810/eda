import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import chi2_contingency, zscore
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import dendrogram, linkage

# Sample dataset for EDA
data = pd.DataFrame({
    'Age': [25, 30, 35, np.nan, 40],
    'Salary': [3000, 4000, 5000, 6000, 7000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male'],
    'City': ['A', 'B', 'A', 'B', 'B']
})

# =========================== STEP 1: Data Understanding and Transformation =========================== #

# 1. Data Types and Summary
print("Data Types:\n", data.dtypes)
print("\nSummary Statistics:\n", data.describe(include='all'))

# 2. Handling Missing Data
imputer = SimpleImputer(strategy='mean')
data['Age'] = imputer.fit_transform(data[['Age']])
print("\nData after Filling Missing Values:\n", data)

# 3. Data Transformation (Scaling)
scaler = MinMaxScaler(feature_range=(-1, 1))
data['Salary_Scaled'] = scaler.fit_transform(data[['Salary']])
print("\nScaled Salary:\n", data[['Salary', 'Salary_Scaled']])

# 4. Z-Score Outlier Detection
data['Salary_ZScore'] = zscore(data['Salary'])
print("\nOutliers Detected (Z-Score):\n", data[data['Salary_ZScore'] > 3])

# =========================== STEP 2: Bivariate and Multivariate Analysis =========================== #

# 5. Correlation Matrix and Heatmap
correlation_matrix = data[['Age', 'Salary']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 6. Scatter Plot
sns.scatterplot(x='Age', y='Salary', hue='Gender', data=data)
plt.title("Age vs Salary Scatter Plot")
plt.show()

# 7. Pair Plot
sns.pairplot(data)
plt.show()

# 8. Chi-Square Test (Categorical Data)
contingency_table = pd.crosstab(data['Gender'], data['City'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print("\nChi-Square Test:\nChi2:", chi2, "p-value:", p)

# =========================== STEP 3: Clustering =========================== #

# 9. K-Means Clustering
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
kmeans = KMeans(n_clusters=2, random_state=42).fit(X)
print("\nK-Means Cluster Centers:\n", kmeans.cluster_centers_)

# 10. Hierarchical Clustering
Z = linkage(X, method='ward')
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()

# =========================== STEP 4: Dimensionality Reduction =========================== #

# 11. PCA
data_pca = pd.DataFrame(np.random.rand(10, 5), columns=['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data_pca)
print("\nPCA Reduced Data:\n", reduced_data)

# =========================== STEP 5: Model Development =========================== #

# 12. Linear Regression
X = data[['Age']].fillna(data['Age'].mean())
y = data['Salary']
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
print("\nLinear Regression Mean Squared Error:", mean_squared_error(y, predictions))

# 13. KNN Classifier
X_knn = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y_knn = [0, 1, 0, 1, 0]
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_knn, y_knn)
print("\nKNN Prediction for [4,5]:", knn.predict([[4, 5]]))

# =========================== STEP 6: Visualization =========================== #

# 14. Box Plot
sns.boxplot(x='Gender', y='Salary', data=data)
plt.title("Salary Distribution by Gender")
plt.show()

# 15. Histogram
sns.histplot(data['Salary'], bins=5, kde=True)
plt.title("Salary Distribution")
plt.show()

# 16. Time Series Plot
time_data = pd.DataFrame({'Date': pd.date_range(start='2023-01-01', periods=10), 'Value': np.random.rand(10)})
time_data.set_index('Date', inplace=True)
time_data.plot(title="Time Series Plot")
plt.show()
