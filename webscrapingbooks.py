#I just want the price,want to be notified when new vampire novels are released from an online bookstore

#Learned:


import requests

from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("ol", class_="row")


books = results.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")



for book in books:
   title_element = book.find("h3", title_="")
   pricing_element = book.find("p", class_="price_color")
   stock_element = book.find("p", class_="instock availability")
   print(title_element.text.strip())
   print(pricing_element.text.strip())
   print(stock_element.text.strip())
   print()
