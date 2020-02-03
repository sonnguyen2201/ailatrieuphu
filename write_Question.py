import json
list=[]
def add(question, a,b,c,d,key,level):
    data = {}
    data['question']=question
    data['a'] = a
    data['b'] = b
    data['c'] = c
    data['d'] = d
    data['key'] = key
    data['level'] = level
    list.append(data)


    


with open('./questions.json','w') as fp:
    json.dump(list,fp)