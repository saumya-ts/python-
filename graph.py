import matplotlib.pyplot as plt


sectors = ['Technology', 'Healthcare', 'Education', 'Finance', 'Manufacturing']
employment = [12.5, 10.8, 7.3, 9.0, 6.2]


plt.figure(figsize=(10, 6))
plt.bar(sectors, employment, color='skyblue')

plt.xlabel('Sectors')
plt.ylabel('Employment (in millions)')
plt.title('Projected Job Employment by Sector')
plt.grid(axis='y', linestyle='--', alpha=0.7)



plt.show()
