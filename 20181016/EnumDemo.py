from enum import Enum, unique

# Month = Enum('Month',('Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# print (Month)
# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)


@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday['Mon'])
print(Weekday(0))
print(Weekday(2).value)
print(Weekday.Fri.value)