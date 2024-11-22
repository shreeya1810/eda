import pandas as pd
import numpy as np
from scipy.stats import mode, zscore

# Input data
data = {'X': [10, 20, 30, 40, 50], 'Y': [5, 15, 25, 35, 45]}
df = pd.DataFrame(data)

# Summary statistics
print("Mean:", df.mean())
print("Median:", df.median())
print("Mode:", df.mode())
print("Variance:", df.var())
print("Standard Deviation:", df.std())

# Covariance and correlation
print("Covariance:\n", df.cov())
print("Correlation:\n", df.corr())

# Outlier detection using Z-score
z_scores = zscore(df)
outliers = np.where(np.abs(z_scores) > 3)
print("Outliers at positions:", outliers)
