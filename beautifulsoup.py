import urllib.request, urllib.parser, urllib.error
import bs4 import BeautifulSoup
url =imput("enter - ")
html =urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parse')
#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href ,None'))
