from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
# custom color hex values
Blue = '#008fd5'
Red = '#fc4f30'
Yellow = '#e5ae37'
Green = '#6d904f'

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']
colors = [Green, Red, Blue ]

plt.stackplot(minutes, player1, player2, player3, labels=labels,
              colors=colors)

# plt.legend(loc='upper left')
# plt.legend(loc='lower left')
plt.legend(loc=(.07, .7))
# legend will be placed 7% from left and
# 70% from bottom
plt.title('Player scrores over each minute')
plt.xlabel('minutes')
plt.ylabel('scores')
plt.tight_layout()
plt.show()