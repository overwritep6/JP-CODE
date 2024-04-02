import requests
import json 

Amount_questions = 10
res = requests.get('https://opentdb.com/api.php?amount='+str(Amount_questions))
response = json.loads(res.text)



def make_file():
    user_questions = open('questions.json','w')
    user_questions.write(json.dumps(response, ensure_ascii=False, indent = 4))


def question_thingy (response):

    data = json.loads(open('questions.json','r').read()) 
    
    try:
        for items in data['results']:
            print(items['type']) 
            print(items['difficulty']) 
            print(items['category']) 
            print(items['question']) 
            print(items['correct_answer']) 
            for items in items['incorrrect_answers']:
                print('Could not find any questions')
                question_thingy(response)
    except:
        print('except fired')
    

    
question_thingy(response)
    



##learn how to randmize an erray##
 