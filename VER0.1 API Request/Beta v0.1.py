import json
import requests

user_selections = { 
    "ammount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php",params=user_selections)
print("response")



