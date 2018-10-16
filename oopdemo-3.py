from types import MethodType


# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value >= 100:
#             raise ValueError('score must between 0~100!')
#         self._score = value

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self,value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2015 -self._birth


# s = Student()
# s.score = 60
# print(s.score)
# # s.score = 1000

# s.birth=1988
# print(s.age)

# s.set_score(100)

# class GraduateStudent(Student):
#     __slots__ = ('score')


# def set_age(self, age):
#     self.age = age


# s = Student()
# s.name = '小明'
# # print(s.name)
# # s.set_age = MethodType(set_age, s)
# # s.set_age(30)
# # print(s.age)

# # s2=Student()
# # # s2.set_age(20)

# # Student.set_age= set_age

# # print(hasattr(s2,'set_age'))
# # s.sex = '男'
# # print(s.sex)
# # s.score =100

# g = GraduateStudent()
# g.score = 99
# # g.sex = '女'


class Screen (object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution==786432:
    print('测试通过！')
else:
    print('测试失败！')
