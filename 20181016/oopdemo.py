std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


class Student(object):

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def print_score(self):
        print('%s : %s' % (self._name, self._score))

    def get_grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 88)
bart.print_score()
lisa.print_score()

print(bart._name, bart.get_grade())
print(lisa._name, lisa.get_grade())

lisa.age = 8
print(lisa.age)
