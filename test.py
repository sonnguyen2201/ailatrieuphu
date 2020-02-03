from db import find_question_set, change


y = find_question_set()
x = y[0]
print(x[4].options)
print('-'*10)

print("TEST 0")
for i in x:
    print(i.content)

print("TEST 1")
x[4].show_content()
x[4].help_audience()
x[4].help_50_50()
x[4].help_audience()
print("TEST 2")
x[2].show_content()
print(x[2].level)
x[2] = change(x[2], y)
x[2].show_content()
print(x[2].level)
