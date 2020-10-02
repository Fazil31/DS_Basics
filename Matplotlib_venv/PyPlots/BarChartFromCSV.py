import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

#plt.style.use("fivethirtyeight")

data = pd.read_csv('../DataFiles/data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

#print(language_counter.most_common(15))

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)
languages.reverse()
popularity.reverse()
# print(languages)
# print(popularity)

plt.barh(languages, popularity)
plt.xlabel('Number of People Who Use')
plt.title('Most Popular Languages')
plt.show()
