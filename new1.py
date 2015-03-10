import urllib
urls = ["http://www.nytimes.com","http://www.CNN.com"]
i=0
while i < len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	print htmltext()
	i=i+1