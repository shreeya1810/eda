from load_data import load_data
import pandas as pd
data = load_data()

# Create bins
bins = [0, 5, 6, 8]
labels = ['Small', 'Medium', 'Large']
data['sepal_length_binned'] = pd.cut(data['sepal_length'], bins=bins, labels=labels)
print("Binned Data:\n", data[['sepal_length', 'sepal_length_binned']].head())
