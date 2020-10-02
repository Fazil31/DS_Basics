from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
title = soup.title.text
# print(title)
# ->finds the first div element using dot notation
# print(soup.div) # finds the first div element

# ->finds the first div element using find() method
# print(soup.find('div'))

# ->finds the first div having class='article'
# print(soup.find('div', class_='article'))

# ->finds the first div having class='footer'
# print(soup.find('div', class_='footer'))
# print(soup.find('div', class_='footer').p)
# print(soup.find('div', class_='footer').text)

# ->Traversing multiple child elements
article = soup.find('div', class_='article')
headline = article.h2.a.text
summary = article.p.text
# print(summary)

# using find_all() method to fetch all elements of a particular type
articles = soup.find_all('div', class_='article')
for article in articles:
    # print(article.h2.a.text)
    # print(article.a.text)
    # print(article.h2.a['href']) # fetching a particular attribute value
    # print(article.p)
    # print(article.p.text)
    pass


#source = requests.get("""https://www.glassdoor.com.au/Salaries/bangalore-data-scientist-salary-SRCH_IL.0,9_IM1091_KO10,24.htm?countryRedirect=true""").text

# When souping (parsing) HTML if you get below error:
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 18505: character maps to <undefined>,
# then use encoding='utf8' parameter
with open('GlassdoorDS.html', encoding='utf8') as glassdoor_file:
    soup1 = BeautifulSoup(glassdoor_file, 'lxml')


all_salaries_by_company = soup1.find('div', id='SalariesByCompany')
job_title = all_salaries_by_company.find('p', class_='m-0').a.text
company = all_salaries_by_company.find_all('p', class_='m-0')[1].text
salary = all_salaries_by_company.find('p', class_='d-block d-md-none m-0').text
range = all_salaries_by_company.find('p', class_='d-block d-md-none m-0 css-1kuy7z7').text
# print(all_salaries_by_company)

for x in all_salaries_by_company.find_all('div', class_='row no-gutters mx-0 py align-items-center css-1u4lhyp'):
    print(f"Job Title: {x.find('p', class_='m-0').a.text}")


