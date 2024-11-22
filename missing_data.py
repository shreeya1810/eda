from sklearn.impute import SimpleImputer
import pandas as pd

# Input data with missing values
data = {'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, 4]}
df = pd.DataFrame(data)

# Global method: Fill with mean
imputer_mean = SimpleImputer(strategy='mean')
df_mean = pd.DataFrame(imputer_mean.fit_transform(df), columns=df.columns)
print("Mean Imputation:\n", df_mean)

# Class-based method: Fill with mode
imputer_mode = SimpleImputer(strategy='most_frequent')
df_mode = pd.DataFrame(imputer_mode.fit_transform(df), columns=df.columns)
print("Mode Imputation:\n", df_mode)
