import json
import random
from help import change, fithty, audiences

def play_game(flag,level, score, helps):
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
        if help_type in helps:
            del helps[help_type]  # loai bo tro giup da duoc su dung
            if help_type == '1':
                fithty(question)
            elif help_type == '2':
                audiences(question)
            else:
                change(lists)
        else:
            print("There is no such help")
    
    user_answer = input("Please input your answer :")
    if user_answer == question['key']:
        print("Your answer is correct")
        score += 1
        level += 1
        print(f"your score is: {score}")
        flag = True
    if user_answer != question['key']:
        print("wrong!")
        print(f"your score is: {score}")