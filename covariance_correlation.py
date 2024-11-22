import numpy as np
import pandas as pd

# Data
data = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# Covariance
print("Covariance:\n", df.cov())

# Correlation
print("Correlation:\n", df.corr())
