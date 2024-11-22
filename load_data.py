import seaborn as sns
import numpy as np

def load_data():
    # Load the Iris dataset
    data = sns.load_dataset("iris")
    
    # Introduce missing values for demonstration
    data.loc[0:4, 'sepal_length'] = np.nan
    
    return data
