import requests
from bs4 import BeautifulSoup

url = ""
r = requests.get("url")
#r.content
soup=BeautifulSoup(r.content)

links=soup.find_all("a")

for link in links:
	print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
	
data = soup.find_all("div", {"class": "xxxxx"})

for item in data:
	print item.contents[0].find_all("a", {"class": "yyyyyy"})[0].text
	print item.contents[1]
	

