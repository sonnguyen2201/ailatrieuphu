from db import find_question_set

official_question, change_question = find_question_set()


def play_game(number, score):
    question = official_question[number-1]
    print(f"Question {number}:")
    question.show_content()

    user_answer = input("Please input your answer :")
    if user_answer == question.answer:
        print("Your answer is correct")
        score += 1
        number += 1
        print(f"your score is: {score}")
    else:
        number = 4
        print("wrong!")

    return (number, score)


if __name__ == "__main__":
    print("Wellcome to Ai La Trieu Phu")
    play = input("Do you want to play ?: ")

    while play == 'y':
        number = 1
        score = 0
        print("Good luck \n")
        while (number < 4):
            number, score = play_game(number, score)
        play = input("Do you want to play ?: ")

    print("Good bye!")
