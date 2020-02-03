from typing import List, Tuple
import json
import random
from question import Question

json_file = open('data.json', encoding='utf-8')
data = json.load(json_file)
questions = data["questions"]


def find_question_set() -> Tuple[List[Question], List[Question]]:
    """
    Find 15 (+ 3) questions:
        - 4 (+ 1) questions level 1: q1, q2, q3, q4, q_change_lv1
        - 5 (+ 1) questions level 2: q5, q6, q7, q8, q9, q_change_lv2
        - 6 (+ 1) questions level 3: q10, q11, q12, q13, q14, q15, q_change_lv3
    """

    # Find 4 questions level 1:
    random.shuffle(questions["level_one"])
    set_q1 = questions["level_one"][:5]
    set_q1 = [Question(**ques) for ques in set_q1]

    # Find 5 questions level 2:
    random.shuffle(questions["level_two"])
    set_q2 = questions["level_two"][:6]
    set_q2 = [Question(**ques) for ques in set_q2]

    # Find 6 questions level 3:
    random.shuffle(questions["level_three"])
    set_q3 = questions["level_three"][:7]
    set_q3 = [Question(**ques) for ques in set_q3]

    official_ques = set_q1[:-1] + set_q2[:-1] + set_q3[:-1]
    change_ques = [set_q1[-1], set_q2[-1], set_q3[-3]]

    return (official_ques, change_ques)


def change(q: Question, q_list: List[Question]) -> Question:
    q_change_list = q_list[1]
    for q_change in q_change_list:
        if q.level == q_change.level:
            return q_change
