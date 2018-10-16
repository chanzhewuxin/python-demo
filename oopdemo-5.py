class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__

s= Student("小红")
print(Student('小明'))
print(s)