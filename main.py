import requests
from bs4 import BeautifulSoup

#user agent must be specified if not the website will refuse connection. 

user_agent = { "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
url = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/all"

response = requests.get(url,headers=user_agent)

print(response)
#print(response.content)

page = BeautifulSoup(response.content, "html.parser")

for item in page.find_all(attrs={"data-auto":"product-tile--title"}):
    print item
