from bs4 import BeautifulSoup
import requests
import re

key_search = input("What job do you want to search for: ")
url = f"https://es.indeed.com/jobs?q={key_search}&l=&fromage=7&from=searchOnDesktopSerp&vjk=0961c2bd93a72336"
page = requests.get(url).text
doc  = BeautifulSoup(page, "html.parser")

print(page)