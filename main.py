import json
import random
from help import fithty, audiences, change
def play_game():
    global flag, score, helps, level
    with open('./questions.json') as qs:
        questions = json.load(qs)
    lists = []
    for i in range(len(questions)-1):
        if questions[i]['level'] == level:
            lists.append(questions[i])
    question = random.choice(lists)
    lists.remove(question)
    print("Question: " + question['question'])
    print("A : "+ question['A'] )
    print("B : " + question['B'])
    print("C: " + question['C'])
    print("D : " + question['D'])
    print("\n")
    help_key = input("Do you need help [y/n]: ")
    if help_key == 'y':
        print("You have below help:")
        for key, values in helps.items():
            print(f'{key}: {values}')
        help_type = input("Please choose the help type: ")
        while help_type not in helps:
            help_type = input("Please choose the help type: ")

        del helps[help_type]  # loai bo tro giup da duoc su dung
        if help_type == '1':
            fithty(question)
        if help_type == '2':
            audiences(question)
        if help_type == '3':
            change(lists)

    user_answer = input("Please input your answer :")
    if user_answer == question['key']:
        print("Your answer is correct")
        print(f"You have {score[level]} USD")
        level += 1
        flag = True
    if user_answer != question['key']:
        print("wrong!")
        if level < 5:
            print(f"your have {score[0]} USD")
        else:
            print(f"your have {score[5]} USD")

print("Wellcome to Ai La Trieu Phu")

score = [0,200,300,500,700,1000,2000,4000,6000,8000,10000]
level = 1
play = input("Do you want to play ?: ")
helps = {'1':'50/50','2':'Audiences','3':'change question','0': 'Exit '}
while play == 'y':
    flag = False
    print("Good luck \n")
    play_game()
    if flag == True:
        if level > 10:
            print("Congrat! You won!")
            break
        play = input("Do you want to continue to play ?: ")
    else:
        
        break
    
print("Good bye!")


 