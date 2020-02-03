from question import Question
from db import find_question_set, change


play = input('Bạn có muốn chơi game không [y/n]:')
if play == 'y':
    print('Trò chơi bắt đầu')
    print('-' * 100)
    print('Câu hỏi 1: Việt Nam có hình chữ gì:')
    print('A: Chữ G')
    print('B: Chữ H')
    print('C: Chữ O')
    print('D: Chữ S')
    user_answer = input('Đáp án bạn chọn là [A/B/C/D]:')
    if user_answer == 'D':
        print('Bạn trả lời đúng.')
    else:
        print('Bạn trả lời sai. Trò chơi kết thúc!')
elif play == 'n':
    print('Trò chơi kết thúc')

q1 = Question(1)
print(q1.content)