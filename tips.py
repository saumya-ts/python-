import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('tip.csv')


fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Exploratory Data Analysis on Tips Dataset')


axs[0, 0].hist(tips['total_bill'], bins=20, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Histogram of Total Bill')
axs[0, 0].set_xlabel('Total Bill')
axs[0, 0].set_ylabel('Frequency')


axs[0, 1].boxplot(tips['tip'], vert=True, patch_artist=True)
axs[0, 1].set_title('Boxplot of Tips')
axs[0, 1].set_ylabel('Tip Amount')


gender_counts = tips['sex'].value_counts()
axs[1, 0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
axs[1, 0].set_title('Gender Distribution')


avg_bill_by_day = tips.groupby('day')['total_bill'].mean()
axs[1, 1].bar(avg_bill_by_day.index, avg_bill_by_day.values, color='mediumseagreen')
axs[1, 1].set_title('Average Total Bill by Day')
axs[1, 1].set_xlabel('Day')
axs[1, 1].set_ylabel('Average Total Bill')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
