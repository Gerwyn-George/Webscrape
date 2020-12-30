import requests
import re



  

headers ={ "user-agent": "mozilla/5.0"}
res = requests.get("https://www.tesco.com/groceries/en-GB/shop/drinks/all", headers=headers)

try:

    for line in res:
        print(line)
    
        x = re.findall("</html>",line)
        if x:
            print(x)
        else:
        pass 

except:

    print("Nevermind")




    



print(res.status_code)
  


