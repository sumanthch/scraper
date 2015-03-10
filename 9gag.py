import urllib
import requests
import bs4 as BS
 
h={'User-Agent': 'Mozilla/5.0'}
url='http://9gag.tv/channel/movie-and-tv'
r=requests.get(url, headers=h)
soup=BS.BeautifulSoup(r.text)
imgs=soup.select('a.img-container')
links = [i['href'] for i in imgs]
n=0
for l in links:
	urllib.urlretrieve(l,"vid"+str(n)+".avi")
	n=n+1
	print "Downloaded %d videos" % n
