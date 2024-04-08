import requests
import json 
import os
import time 

def new_user():
    username = input("What Would you Like you Username to be.")
    usernames = open('usernames.json', 'w')
    usernames = json.loads(usernames)
    usernames.append(username)
    

def make_file():
    user_questions = open('questions.json','w')
    user_questions.write(json.dumps(response, ensure_ascii=False, indent = 4))
    amount_questions = 10
    res = requests.get('https://opentdb.com/api.php?amount='+str(amount_questions)+'&category=9&difficulty=easy&type=multiple')
    response = json.loads(res.text)
    return response


def question_thingy ():
    data = json.loads(open('questions.json','r').read()) 
    for items in data['results']:
        print(items['type']) 
        print(items['difficulty']) 
        print(items['category']) 
        print(items['question']) 
        print(items['correct_answer']) 
        for answers in items['incorrect_answers']:
            print(answers)


def main_menu():
    menu = {}
    menu['1']='1:New user'
    menu['2']='2:Remove User'
    menu['3']='3:Start Quiz'
    menu['4']='4:End Quiz'
    print('Use Intagers To Navigate Around The Menus')
    time.sleep(3)
    os.system('cls')    
    while True:
        options=menu.keys()
        sorted(options)
        for entry in options:
            print (menu[entry])
        selection=input('Please Select:')
        if selection =='1':
            print('1:New user')
            new_user()
        elif selection == '2':
            print('2:Remove User')
        elif selection == '3':
            print('3:Starting Quiz')
            question_thingy()        
        elif selection == '4':
            print('4:End Quiz')      
        else:
            print("you are gay select something correct")  


main_menu()

    



##learn how to randmize an erray##
