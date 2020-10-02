from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
# custom color hex values
Blue = '#008fd5'
Red = '#fc4f30'
Yellow = '#e5ae37'
Green = '#6d904f'

df = pd.read_csv('../DataFiles/salary_data.csv')
ages = df['Age']
dev_salaries = df['All_Devs']
py_salaries = df['Python']
js_salaries = df['JavaScript']
overall_median_salary = 57287

# plot 1
plt.plot(ages, dev_salaries, color='#444444', linestyle='--',
         linewidth=1, label='All Devs')
# plot 2
plt.plot(ages, py_salaries, label='Python', linewidth=1)

# fill_between 1
plt.fill_between(ages, py_salaries, overall_median_salary,
                 interpolate=True, alpha=0.3,
                 where=(py_salaries > overall_median_salary))

# fill_between 2
# plt.fill_between(ages, py_salaries, overall_median_salary,
#                  interpolate=True, alpha=0.3,
#                  where=(py_salaries <= overall_median_salary))

# fill_between 3
plt.fill_between(ages, py_salaries, dev_salaries, label='Py above All',
                 interpolate=True, alpha=0.7, color=Green,
                 where=(py_salaries > dev_salaries))

# fill_between 4
plt.fill_between(ages, py_salaries, dev_salaries, label='Py below All',
                 interpolate=True, alpha=0.5, color=Red,
                 where=(py_salaries <= dev_salaries))

plt.legend(loc=(0.07, 0.70))
plt.title('Developers Median Salary (USD)')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.tight_layout()
plt.show()