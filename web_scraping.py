from bs4 import BeautifulSoup
import requests

url = "https://www.game.es/OFERTAS/PACK/PACKS/PLAYSTATION-5-SLIM-STELLAR-BLADE/P05166"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="€")
#parent = prices[1].parent
print(prices)
