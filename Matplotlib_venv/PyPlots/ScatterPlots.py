from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')
# custom color hex values
Blue = '#008fd5'
Red = '#fc4f30'
Yellow = '#e5ae37'
Green = '#6d904f'

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 1000]

# Scatter Plot 1
# plt.scatter(x, y , s=sizes,  c=colors, cmap='Greens', marker='.',
#             edgecolor='black', linewidth=1,  alpha=0.75)
#
# cbar = plt.colorbar()
# cbar.set_label('satisfaction level')

# Scatter Plot 2
df = pd.read_csv('../DataFiles/2019-05-31-data.csv')
views = df['view_count']
likes = df['likes']
ratio = df['ratio']

plt.scatter(views, likes, s=100, c=ratio, cmap='summer', marker='.',
            edgecolor='black', linewidth=1, alpha=0.5)

plt.xscale('log')
plt.yscale('log')

cbar = plt.colorbar()
cbar.set_label('Likes to Dislikes Ratio')

plt.legend()
plt.title('Trending Youtube Videos')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
plt.show()