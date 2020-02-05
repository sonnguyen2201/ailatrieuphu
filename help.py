import random
def fithty(question):
    option = ['A','B','C','D']
    answer = question['key']
    var = random.choice(option)
    while var == answer:
        var = random.choice(option)
    print(f"question: {question['question']} \n")
    for c in option:
        if c == var or c == answer:
            print(f'{c}: {question[c]}')

def change(lists):
    question_new = random.choice(lists)
    print("Question: " + question_new['question'])
    print("A : "+ question_new['A'] )
    print("B : " + question_new['B'])
    print("C: " + question_new['C'])
    print("D : " + question_new['D'])

def audiences(question):
    option = ['A','B','C','D']
    option_per = {}
    an = question['key']
    total = 100
    for c in option:
        if c != question['key']:
            option_per[c] = random.randrange(20)
            total -= option_per[c]
    option_per[an] = total
    for c in option:
        print(f'option {c}: {option_per[c]}')
