#I want to be notified when new vampire novels are released from an online bookstore



import requests

from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("ol", class_="row")


books = results.find_all("article", class_="product_pod")



for book in books:
   # pricing_element = book.find("p", class_="price_color")
    rating_element = book.find("p", class_="star-rating Three")
    #print(pricing_element.text.strip())
    print(rating_element.text.strip())


