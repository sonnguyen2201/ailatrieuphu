from typing import List, Tuple
from question import Question


class User:
    state = True  # False ~ lose the game
    money = 0
    curr_ques = 1

    def pass_q(self, q: Question):
        pass
