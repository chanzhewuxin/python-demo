# import urllib
#
# response = urllib.urlopen('http://baidu.com')
#
# print (response.read())

# a= 123 # a 是整数

# print(a)

# def show(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print(show(112))

# names = ['Michel', 'Bob', 'Tracy']
#
# for name in names:
#     print(name)
#
#     sum = 0
#
# for x in [1, 2, 3, 4, 5, 6, 7, 8]:
#     sum = sum + x
#     print(sum)
#
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)
#
# sum = 0
# n = 99
#
# while n > 0:
#     if sum > 20:
#         break
#     sum = sum + n
#     n = n - 2
# print(sum)
#
# d={'Marchil':90,'Bob':20,'Tracy':20}
# for i in d:
#     print(i)
#
# s=set([5,1,1,3,4])
# s.add(0)
# l =[4,5,9,1,3,4,6]
# print(s)
# l.sort()
# l[1]='aa'
# print('l:',l)

# def power(x):
#     print (x*x)
#
# power(9)

# def add_end(L=None):
#     if L is None:
#         L=[]
#     L.append('End')
#     return L
# print(add_end([1,2,3]))
#
# print(add_end(['x','u','z']))
#
# print(add_end())
#
# print(add_end())

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# # print(calc([1,2,3]))
# # print(calc([1,3,5,7]))
# # print(calc((1,2,3)))
# print(calc(1,3,4,5))
# print(calc(*[1,3,4,5]))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# print(person('Mihcal',30))
person('Michal', 30)
person('Bob',39,city='Beijing')
