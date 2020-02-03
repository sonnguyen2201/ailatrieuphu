import random


class Question:
    def __init__(self, content=None, A=None, B=None, C=None, D=None, answer=None, level=None):
        self.content = content
        self.options = [[A, 'A', 0], [B, 'B', 0], [C, 'C', 0], [D, 'D', 0]]
        self.answer = answer
        self.level = level

    def show_content(self):
        print(self.content)
        for i in self.options:
            print(f'Đáp án {i[1]}: {i[0]}')

    def help_50_50(self):
        retain = []

        for i in self.options:
            if i[1] == self.answer:
                retain.append(i)
                del i

        random.shuffle(self.options)
        retain.append(self.options[0])
        self.options = retain

    def help_audience(self):
        total = 100
        for i in range(len(self.options)):
            if self.options[i][1] != self.answer:
                self.options[i][2] = random.randrange(23) if (len(self.options) == 4) else random.randrange(45)
                total = total - self.options[i][2]

        for i in range(len(self.options)):
            if self.options[i][1] == self.answer:
                self.options[i][2] = total

        for i in self.options:
            print(f'Đáp án {i[1]}: {i[0]} ---> Chiếm {i[2]}%')
