import urllib.request
import time

price= 99.99
while price > 4.74:
  time.sleep(15)
  page= urllib.request.urlopen("file:///F:/Claudy/Study/CS/Developing/praxis/testing/Python/prices-royalty.html")
  text= page.read().decode("utf8")
  search_str= ">$"
  str_length= 4;
  pos= text.find(search_str)+len(search_str)
  price=float(text[pos:pos+str_length])
print("price= "+str(price)+" Buy!!!")