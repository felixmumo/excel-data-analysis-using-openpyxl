import pandas as pd
import matplotlib.pyplot as plt

# Read data (choose ONE)
#data = pd.read_csv('data.csv')
data = pd.read_excel('pie_chart_data.xlsx')

# Extract values
labels = data['Fruit']
sizes = data['Quantity']

# Custom colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Explode first slice
explode = (0.1, 0, 0, 0)

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True
)

# Title
plt.title('Fruit Distribution')

# Keep pie circular
plt.axis('equal')

# Save the chart
plt.savefig('pie_chart.png', dpi=300)

# Show chart
plt.show()
