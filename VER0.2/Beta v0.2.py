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
    for i in range(len(question["incorrect_answers"])):
        print(f"{i+1}. {question['incorrect_answers'][i]}")
    print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == len(question["incorrect_answers"]) + 1:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect.")
    
