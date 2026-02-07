import pandas as pd
import matplotlib.pyplot as plt 
import openpyxl

# Read data from Excel file
data = pd.read_excel('data.xlsx')
# Display the data
print(data)
#bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['Category'], data['Value'], color='skyblue')
plt.title('Bar Chart from Excel Data')
plt.xlabel('Category')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png', dpi=300)
plt.show()
