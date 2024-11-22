from load_data import load_data
# Branching
data = load_data()
if data['sepal_length'].mean() > 5:
    print("Sepal length mean is greater than 5")
else:
    print("Sepal length mean is less than or equal to 5")

# Looping
for species in data['species'].unique():
    print(f"Species: {species}, Count: {data[data['species'] == species].shape[0]}")
