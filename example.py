import urllib
import requests
from bs4 import BeautifulSoup

url = urllib.urlopen("http://9gag.com/fresh")
text = url.read()
soup = BeautifulSoup(text)

images=soup.select("img")

links = [i['src'] for i in images]
n=0
for l in links:
	urllib.urlretrieve("l","image %d") % n
	n=n+1
	print "Downloaded %d images" % n

