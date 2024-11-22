import numpy as np

# Deduplication
data = pd.DataFrame({"ID": [1, 2, 2, 3], "Value": [10, 20, 20, 30]})
data = data.drop_duplicates()
print("Deduplicated Data:\n", data)

# Replacing values
data['Value'] = data['Value'].replace(10, 100)
print("Replaced Values:\n", data)

# Binning
bins = [0, 15, 25, 35]
labels = ['Low', 'Medium', 'High']
data['Category'] = pd.cut(data['Value'], bins=bins, labels=labels, include_lowest=True)
print("Binned Data:\n", data)
