import matplotlib.pyplot as plt


sectors = ['Technology', 'Healthcare', 'Education', 'Finance', 'Manufacturing']
employment = [12.5, 10.8, 7.3, 9.0, 6.2]
colours=["purple","skyblue","lightgreen","lavender","orange"]
plt.figure(figsize=(10, 10))

plt.subplot(2,2,1)
plt.plot(sectors, employment, color='skyblue')
plt.xlabel('Sectors')
plt.ylabel('Employment')
plt.title('Projected Job Employment by Sector Form of line')
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.subplot(2,2,2)
plt.bar(sectors, employment, color='skyblue')
plt.xlabel('Sectors')
plt.ylabel('Employment')
plt.title('Projected Job Employment by Sector Form of Bar Chart')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplot(2,2,3)
plt.pie(employment,labels=sectors,colors=colours,autopct=" %1.1f%% ")
plt.title('Projected Job Employment by Sector Form of Pie Chart')


plt.tight_layout()
plt.show()
