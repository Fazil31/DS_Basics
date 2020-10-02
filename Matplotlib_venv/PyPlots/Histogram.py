from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
# custom color hex values
Blue = '#008fd5'
Red = '#fc4f30'
Yellow = '#e5ae37'
Green = '#6d904f'

ages = [18, 19, 21, 25, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# bins = [20, 30, 40, 50, 60]

df = pd.read_csv('../DataFiles/ages_data.csv')
ids = df['Responder_id']
ages = df['Age']
median_age = 29

# plt.hist(ages, bins= 5, edgecolor='black')
plt.hist(ages, bins=bins, edgecolor='black', log=True)
plt.axvline(median_age, color=Red, linewidth=1, label='median age')
plt.legend()
plt.xlabel('Age')
plt.ylabel('Number of Respondents')
plt.tight_layout()
plt.show()