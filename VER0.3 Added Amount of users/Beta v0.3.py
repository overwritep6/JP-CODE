import requests
import json 
import html

#username array
usernames = []

#amount of questions
Amount_questions = 10

#Gets the Api questions and puts it into questions json file
url = "https://opentdb.com/api.php?amount=10"
response = requests.get((url)+str(Amount_questions))
api_data = json.loads(response.text)
make_json = open('questions.json','w')
user_questions = api_data['results']

#def make_file():
    #user_questions = open('questions.json','w')
    #user_questions.write(json.dumps(api_data, ensure_ascii=False, indent = 4))

def how_many_playing():
    user_amount = int(input('how many users are playing: '))
    #user_amount -=1
    def asking_thing():
        username = input('what your name: ')
        usernames.append([username,0,0])
    for number in range(int(user_amount)):
        asking_thing()

#question asking fuction
def question_asker():

    
    for question in user_questions:
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




#def question_sorter(api_data):
    #data = json.loads(open('questions.json','r').read()) 
    data = api_data
    try:
        for items in data['results']:
            print(items['type']) 
            print(items['difficulty']) 
            print(items['category']) 
            print(items['question']) 
            print(items['correct_answer']) 
            for items in items['incorrrect_answers']:
                print('Could not find any questions')
                question_sorter(api_data)
    except:
        print('except fired')
    

#make_file()
question_asker()
print()



##learn how to randmize an erray##
 