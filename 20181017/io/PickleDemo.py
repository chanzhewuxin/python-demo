import pickle
import os
import json

d = dict(name='Bob', age=20, score=99)
# print(pickle.dumps(d))

# with open('c:/GitHub/python-demo/20181017/io/dump.txt', 'wb') as f:
#     pickle.dump(d, f)

# print(json.dumps(d))

# json_str = '{"age":20,"name":"daniel","score":100}'
# j =json.loads(json_str)
# print(j['age'])

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

s=Student('小明',20,69)
print(json.dumps(s,default=student2dict))