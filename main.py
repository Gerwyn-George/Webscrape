from urllib.request import Request, urlopen

 

def Collect_Webpage(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    html = page.read().decode("utf-8")

    print(html)
  
print("Intialising")
Collect_Webpage("https://www.tesco.com/groceries/en-GB/shop/fresh-food/fresh-fruit/bananas")
  


