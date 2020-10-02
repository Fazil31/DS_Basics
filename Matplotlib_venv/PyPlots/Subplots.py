import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('../DataFiles/salary_data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
fig2, axx = plt.subplots(nrows=2, ncols=1, sharey=True)


ax1.plot(ages, py_salaries, label='Python')
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax2.legend()
# ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

axx[0].plot(ages, js_salaries, label='JavaScript')
axx[1].plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')


axx[0].legend()
axx[1].set_title('Median Salary (USD) by Age')
# ax3.set_xlabel('Ages')
axx[0].set_ylabel('Median Salary (USD)')

axx[1].legend()
# ax4.set_title('Median Salary (USD) by Age')
axx[1].set_xlabel('Ages')
axx[1].set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()