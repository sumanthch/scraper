import urllib
import requests
import bs4 as BS
 
h={'User-Agent': 'Mozilla/5.0'}
url='http://reddit.com/r/pics'
r=requests.get(url, headers=h)
soup=BS.BeautifulSoup(r.text)
imgs=soup.select('a.thumbnail.may-blank')
links = [i['href'] for i in imgs]
n=0
for l in links:
	urllib.urlretrieve(l,"img"+str(n)+".jpg")
	n=n+1
	print "Downloaded %d images" % n