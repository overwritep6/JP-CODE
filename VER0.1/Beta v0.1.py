import json
import requests

API_URL = "https://opentdb.com/api.php?amount=10"

response = requests.get(API_URL)
api_data = json.loads(response.text)

user_questions = api_data["results"]

correct_answers = 0
for question in user_questions:
    print(question["question"])
    print("Options:")

    
