import requests
import json 
import os
import time 
 
 
def make_file():
    user_questions = open('questions.json','w')
    user_questions.write(json.dumps(response, ensure_ascii=False, indent = 4))
    Amount_questions = 10
    res = requests.get('https://opentdb.com/api.php?amount='+str(Amount_questions))
    response = json.loads(res.text)
    return response

def question_thingy (response):

    data = json.loads(open('questions.json','r').read()) 
    for items in data['results']:
        print(items['type']) 
        print(items['difficulty']) 
        print(items['category']) 
        print(items['question']) 
        print(items['correct_answer']) 
        for awnsers in items['incorrect_answers']:
            print('Could not find any questions')
            question_thingy(response)
    
def main_menu():
    menu = {}
    menu['1']='Add user'
    menu['2']='Delete User'
    menu['3']='Start Quiz'
    menu['4']='End Quiz'
    print('Use Intagers To Navigate Around The Menus')
    time.sleep(5)
    os.system('cls')    
    while True:
        options=menu.keys()
        sorted(options)
        for entry in options:
            print (menu[entry])

        selection=input('Please Select:')
        if selection =='1':
            print('1:Add user')
        elif selection == '2':
            print('2:Delete User')
        elif selection == '3':
            print('3:Starting Quiz')
            question_thingy(response)        
        elif selection == '4':
            print('4:End Quiz')      
        else:
            print("you are gay select something correct")  


main_menu()
    



##learn how to randmize an erray##
 