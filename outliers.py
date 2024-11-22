from scipy.stats import zscore

# Data
data = [10, 12, 12, 13, 14, 100]
z_scores = zscore(data)
outliers = [i for i, z in enumerate(z_scores) if abs(z) > 3]
print("Outliers:", outliers)
