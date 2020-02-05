import json
import random
from Play import play_game

print("Wellcome to Ai La Trieu Phu")

score = 0
level = 1
play = input("Do you want to play ?: ")
helps = {'1':'50/50','2':'Audiences','3':'change question'}
while play == 'y':
    flag = False
    print("Good luck \n")
    play_game(flag,level,score,helps)
    if flag == True:
        if level > 10:
            print("Congrat! You won!")
            break
        play = input("Do you want to continue to play ?: ")
    else:
        print("Sao lai vao day!")
        break
    
print("Good bye!")


 