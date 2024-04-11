import json
import requests

#takes the api reponse and puts it into response the using api_data it puts it into a text format 
#from where it puts it into user questions.
url = "https://opentdb.com/api.php?amount=10"
response = requests.get(url)
api_data = json.loads(response.text)
user_questions = api_data['results']

#track the number of incorrect and correct answers.
incorrect_answers = 0
correct_answers = 0

#takes the API data and prints it into a readable format witch then it after prints the awnsers 
#and lets  the user pick one in witch the it either displays incorrect or correct and adds 1 to
#the respective score
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
        incorrect_answers += 1
    
