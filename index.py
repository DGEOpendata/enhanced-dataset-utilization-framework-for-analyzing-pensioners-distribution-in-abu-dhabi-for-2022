python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming the dataset is downloaded and saved locally)
data_path = 'Distribution_of_Pensioners_2022.xlsx'
data = pd.read_excel(data_path, sheet_name='Sheet1')

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Example: Analyze the total number of pensioners per quarter
total_per_quarter = data.groupby('Quarter')['Total'].sum()
print("Total Pensioners per Quarter:")
print(total_per_quarter)

# Plot the data
total_per_quarter.plot(kind='bar', color='skyblue', title='Total Pensioners per Quarter (2022)')
plt.xlabel('Quarter')
plt.ylabel('Total Pensioners')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('total_pensioners_per_quarter.png')
plt.show()
