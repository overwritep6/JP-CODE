import requests

#takes the api and prints it.
url = "https://opentdb.com/api.php?amount=10"
response = requests.get(url).json()
print(response)



