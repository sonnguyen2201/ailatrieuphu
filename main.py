import json
def play_game(flag,level, score):
    with open('./questions.json') as qs:
        questions = json.load(qs)
    for i in range(len(questions)-1):
        if questions[i]['level'] == level:
            question = questions[i]

    print("Question: " + question['question'])
    print("A : "+ question['a'] )
    print("B : " + question['b'])
    print("C: " + question['c'])
    print("D : " + question['d'])
    print("\n")
    user_answer = input("Please input your answer :")
    if user_answer == question['key']:
        print("Your answer is correct")
        score += 1
        level += 1
        print("your score is: %d") %(score)
        flag = True
    else:
        flag = False
        print("wrong!")

print("Wellcome to Ai La Trieu Phu")

score = 0
level = 1
play = input("Do you want to play ?: ")
while play == 'y':
    flag = True
    print("Good luck \n")
    play_game(flag,level,score)
    if flag is True:
        play = input("Do you want to play ?: ")
    else:
        break
    
print("Good bye!")
 