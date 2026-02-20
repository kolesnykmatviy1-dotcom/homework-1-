import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")

    prices = soup.find_all("p", class_="price_color")

    for price in prices:
        print(price.text)
else:
    print("error")