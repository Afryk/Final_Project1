import matplotlib.pyplot as plt
import pandas as pd



x = []
y = []

Po = pd.read_csv('scraped_data.csv')
all_values = Po.groupby("Pollutant")["Value"].apply(list)

avg_values = Po.groupby("Pollutant")['Value'].mean()
print(avg_values)

x = avg_values.index
y = avg_values.values


plt.bar(x, y, color='g', width=0.72, label='Average values')
plt.xlabel('Pollutant')
plt.ylabel('Average Value')
plt.title("Average Pollutants values in Lithuania")
plt.show()




po = pd.read_csv('scraped_data.csv')
avg_values = po.groupby("Pollutant")['Value'].mean().reset_index()
print(avg_values)
colors = ['firebrick', 'brown', 'red', 'sienna', 'peru', 'peachpuff']
fig1, ax1 = plt.subplots()
ax1.pie(avg_values['Value'], labels=avg_values['Pollutant'], colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.title("Average Pollutants procentage in Lithuania")
plt.tight_layout()
plt.show()



po = pd.read_csv('output.csv')
avg_values = po.groupby("Pollutant")['Value'].mean().reset_index()
print(avg_values)
colors = ['firebrick', 'brown', 'red', 'sienna', 'peru', 'peachpuff']
fig1, ax1 = plt.subplots()
ax1.pie(avg_values['Value'], labels=avg_values['Pollutant'], colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.title("Average Pollutants procentage in Lithuania")
plt.tight_layout()
plt.show()







Po = pd.read_csv('output.csv')

city_values = Po.groupby("City")['Value'].mean()
print(city_values)

x = city_values.index
y = city_values.values


plt.bar(x, y, color='g', width=0.72, label='Pullutant')
plt.xlabel('City')
plt.ylabel('Pullutant amount')
plt.title("Average Pollutants values in Lithuanian Cities")
plt.show()



