from selenium import webdriver
from bs4 import BeautifulSoup
import csv

#Step1: - Import the driver
driver = webdriver.Chrome("C:/Users/ahmad.idrees/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe")

#Step2: - Hit the website
driver.get("http://www.values.com/inspirational-quotes")

#Step3: - Get the Html Content
content = driver.page_source

#Step4: - Parse the Html
soup = BeautifulSoup(content, 'html.parser')

#Step5: - HTML Tree Travesal

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'all_quotes'})

for row in table.findAll('div',
                         attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

#Step6: - Appending the Quotes
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
