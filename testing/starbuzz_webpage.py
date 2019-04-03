import urllib.request
import urllib.parse
import time

def get_price():
	page= urllib.request.urlopen("file:///D:/Developing/praxis-master/testing/prices.html")
	text= page.read().decode("utf8")
	find_str=">$"
	price_length=4
	price_pos=text.find(find_str)+len(find_str)
	price=float(text[price_pos:price_pos+price_length])
	return price

def set_password():
	password="C8H10N402"

def send_to_twitter(price):
	msg= "I am indeed a better message xD #bettermessage"
	# password_manager= urllib.request.HTTPPasswordMgr()
	# password_manager.add_password("Twitter API", "http://twitter.com/statuses", "claudy_mr", "testingmono01")
	# http_handler= urllib.request.HTTPBasicAuthHandler(password_manager)
	# page_opener= urllib.request.build_opener(http_handler)
	# urllib.request.install_opener(page_opener)
	# params= urllib.parse.urlencode({'status':msg}).encode("utf-8")
	# params= urllib.parse.urlencode({'status':msg})
	# resp= urllib.request.urlopen("http://twitter.com/statuses/update.json/"+params)
	# resp.read()
	# print(params)
	print(msg)
	print("Price: "+str(price))



# password=""
# set_password()
price_desired=4.74
price_required=input("You want the price now? (Y/N) ").upper()
if price_required=="Y":
	# print(get_price())
	send_to_twitter(get_price())
else:
	price=price_desired+1
	while price > price_desired:
		time.sleep(3)
		price= get_price()
	# print(price)
	# print("Buy!!!")
	send_to_twitter(price)
