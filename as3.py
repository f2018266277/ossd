from bs4 import BeautifulSoup
import requests

url="https://go.drugbank.com/covid-19#drugs"

req = requests.get(url)
soup = BeautifulSoup(req.text)
for i in soup.find_all('strong',limit=13)[3:]:
  print(i)