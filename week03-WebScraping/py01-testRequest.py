
import requests

from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print (page)

print("-------------------")

print (page.content)


