from load_data import load_data
from load_data import load_data
import pandas as pd
import matplotlib.pyplot as plt

# Sample time series data
data = {'Date': pd.date_range(start='1/1/2023', periods=10), 'Value': [10, 12, 14, 13, 15, 16, 14, 12, 13, 14]}
df = pd.DataFrame(data)

# Line plot
plt.plot(df['Date'], df['Value'], marker='o')
plt.title("Time Series Plot")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.show()
