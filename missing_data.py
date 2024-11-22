from load_data import load_data
data = load_data()
data.loc[0:4, 'sepal_width'] = np.nan
data['sepal_width'] = imputer.fit_transform(data[['sepal_width']])
print("Missing values filled:\n", data.head())
