import urllib
import requests
from bs4 import BeautifulSoup

url = urllib.urlopen("http://9gag.com/fresh")
text = url.read()
soup = BeautifulSoup(text)

images=soup.select("img")

links = [i['src'] for i in images]
n=0
for l in links[1:]:
	urllib.urlretrieve(l,"image"+str(n)+".jpg")
	n=n+1
	print "Downloaded %d images" % n
