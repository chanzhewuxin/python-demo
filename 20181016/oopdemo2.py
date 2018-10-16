import types

# print(type(123))
# print(type(abs))
# print(type(None))
# print(type(123) == type(456))


def fn():
    pass


# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x: x) == types.LambdaType)
# print(type(lambda x: x) == types.FunctionType)
# print(type(lambda x: x) == types.BuiltinFunctionType)
# print(type((x for x in range(10))) == types.GeneratorType)

# print(dir('abc'))
# print(dir(types))

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x*self.x

# obj = MyObject()
# print(hasattr(obj,'x'))
# print(hasattr(obj,'y'))
# print(getattr(obj,'x'))
# # print(getattr(obj,'y'))
# print(setattr(obj,'y',199))
# # print(hasattr(obj,'y'))
# print(obj.y)

class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count +=1

std1=Student('小明')
std2=Student('小红')
print(Student.count)