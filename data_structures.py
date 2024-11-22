from load_data import load_data
# Lists
my_list = list(data['species'].unique())
print("List of unique species:", my_list)

# Dictionaries
species_count = data['species'].value_counts().to_dict()
print("Species count:", species_count)
