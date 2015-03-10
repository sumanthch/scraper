import urllib
import requests
import bs4 as BS
 
h={'User-Agent': 'Mozilla/5.0'}
url='http://9gag.com/fresh'
r=requests.get(url, headers=h)
soup=BS.BeautifulSoup(r.text)
imgs=soup.select('img.badge-item-img')
links = [i['src'] for i in imgs]
n=0	 
for l in links:
	if n < 5:
		urllib.urlretrieve(l,"img"+str(n)+".jpg")
		n=n+1
		print "Downloaded %d images" % n
