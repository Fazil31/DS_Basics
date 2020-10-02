from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
# Colors hex values:
Blue = '#008fd5'
Red = '#fc4f30'
Yellow = '#e5ae37'
Green = '#6d904f'

# Pie-Chart 1
slices = [120, 80, 30, 20]
labels = ['Py', 'Js', 'C#', 'J']
# colors = ['Blue', 'Red', 'Green', 'Yellow']
colors = [Blue, Red, Green, Yellow]
# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'Black'})


# Pie-Chart 2  (pie-charts are good to compare just a hand full of values, and not too many like below)
# slices1 = [5833, 7201, 7331, 7920, 18017, 18523, 20524, 23030, 27097, 31991, 35917, 36443, 47544, 55466, 59219]
# labels1 = ['Assembly', 'Go', 'Ruby', 'Other(s):', 'C', 'TypeScript', 'C++', 'PHP', 'C#', 'Bash/Shell/PowerShell', 'Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
# plt.pie(slices1, labels=labels1)

# Pie-Chart 3
slices2 = [35917, 36443, 47544, 55466, 59219]
labels2 = ['Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
explode = [0, 0.1, 0, 0, 0]
plt.pie(slices2, labels=labels2, explode=explode, startangle=180, shadow=True, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'Black'})


plt.title('Popular Programming Languages Proportion')
plt.tight_layout()
plt.show()