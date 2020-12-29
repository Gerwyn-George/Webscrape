from urllib.request import urlopen
 

def Collect_Webpage(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")

    for line in html:
        print("hello")

    print(html)


    
Collect_Webpage("https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse")
