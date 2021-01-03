import requests
from bs4 import BeautifulSoup
from time import sleep
import re

#user agent must be specified if not the website will refuse connection. 

user_agent = { "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

url = "https://www.tesco.com/groceries/en-GB/shop/fresh-food/all"

product = []
price = []

def get_product_name(page):

    for item in page.find_all(attrs={"data-auto":"product-tile--title"}):

        product.append(item.text)
        
    return product

def get_product_price(page):

    for item in page.find_all(attrs={"data-auto":"price-value"}):
      
        price.append(item.text)
    return price

def check_product_range(url):

    original_url = url + "?page="

    for i in range(1,999):

        url = original_url + str(i) 
         
        response = requests.get(url,headers=user_agent)
        page = BeautifulSoup(response.content, "html.parser")
        
        sleep(1)
        if response.status_code == 200:
            print(url)
            get_product_name(page)
           
        else:
            break 

check_product_range("https://www.tesco.com/groceries/en-GB/shop/fresh-food/all") 
    
print(product)
#get_product_name(page)
#get_product_price(page)

#print price[0]


    


