import requests
import json

url = 'https://xxxxxxxxx.xx'

name="ticket automatique"
content="ouverture d\'un incident"
itilcat=7
statut=6
xtyp=2


apptoken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

url = f'{url}/apirest.php/initSession'
headers = {"Content-Type" : "application/json",
           "Authorization" : "user_token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
           "App-Token" : apptoken
           }


r = requests.get(url, headers=headers)
x = json.loads(r.text)
print(x["session_token"])


url = f'{url}/apirest.php/Ticket'
headers = {"Content-Type" : "application/json",
           "Session-token" : x["session_token"],
           "App-Token" : apptoken
           }
myData = "{'input': [{'name' :  {0}  , 'content' : , 'itilcategories_id' : , 'statut' : ,'type' :  }]}".format("ticket automatique")

print(myData)

r = requests.post(url, headers=headers, data=myData)
print(r)