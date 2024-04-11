from os import system, name
from time import sleep
import requests
import json 
import html


usernames = []

#catagory 15 is entertainment and gatgory 18 is Scienc: computers catagory and 9 is general knowlege 21 is sports
custom_quiz = [["Custom selections:",["Catagory: ","Science: Computers","Entertainment: Video Games","General Knowledge"]],["Difficulty: ",["easy","medium","hard","any"]],["Type: ",["multiple","boolean","either"]]]
catagory = ("&catagory=15")
difficulty = ("&difficulty=easy")

def clear():
    if name == 'nt':
        os = system('cls')
    else:
        os = system('clear')
 
def question_grabber(catagory,difficulty):
    url = "https://opentdb.com/api.php?amount=10"
    response = requests.get((url)+str(catagory)+str(difficulty))
    api_data = json.loads(response.text)

    make_json = open('questions.json','w')
    make_json.write(json.dumps(api_data, ensure_ascii=False, indent = 4))



def how_many_playing():
    user_amount = int(input('how many users are playing: '))
    #user_amount -=1
    def asking_thing():
        username = input('what your name: ')
        usernames.append([username,0,0])
    for number in range(int(user_amount)):
        asking_thing()



def question_asker():
    with open('questions.json') as json_file:
        questions = json.load(json_file)   
        for question in questions["results"]:
            clear()
            print(html.unescape(question["question"]))
            print(html.unescape("Options:"))
            for i in range(len(question["incorrect_answers"])):
                print(html.unescape(f"{i+1}. {question['incorrect_answers'][i]}"))
            print(html.unescape(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}"))
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer == len(question["incorrect_answers"]) + 1:
                print("Correct!")
            else:
                print("Incorrect.") 



question_grabber(catagory,difficulty)
question_asker()




##learn how to randmize an erray##
