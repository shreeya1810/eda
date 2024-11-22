from load_data import load_data
from sklearn.impute import SimpleImputer
data = load_data()
# Fill missing values
imputer = SimpleImputer(strategy='mean')
data['sepal_length'] = imputer.fit_transform(data[['sepal_length']])
print("Missing values handled:\n", data.head())
