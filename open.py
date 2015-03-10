import urllib
htmlfile = urllib.urlopen("http://9gag.com")
htmltext = htmlfile.read()
print htmltext