import urllib.request

page= urllib.request.urlopen("file:///F:/Claudy/Study/CS/Developing/praxis/testing/Python/prices.html")
text= page.read().decode("utf8")
price= text[219:223]
print(price)