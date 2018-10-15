# 数组
# classmates = ['','Bob','Tracy',1,['asp','jsp'],True]
# classmates.append('aaaa')
# classmates.insert(1,'jack')
# print(classmates)
# print(len(classmates))
# print(classmates[-1])
# print(classmates.pop())
# print(classmates)

# # Tuple
# classmates1=('Michael','Bob','Tracy')
# print(classmates1)
# # classmates1[0]=1;
# print (classmates1[1])
# print((1))
# print((1,))

# L=[['Apple','Google','Microsoft'],['Java','PHP','Ruby','Python'],['Adam','Bart','Lisa']]

# print(L[0][0])
# print(L[1][3])
# print(L[2][2])

# age = 2
# if age>1:
# 	print('aaa')
# else:
# 	print('bbb')

# if age>=1:
# 	print("age is one.")
# elif age<0:
# 	print("age is less than one .")
# else :
# 	print ("age is other number.")

# s=input('birth:')
# brith=int(s)

# if brith<2000:
# 	print('00前')
# else:
# 	print('00后')

# names=['Micheal','Bob','Tracy']
# for name in names:
# 	print (name)

# d={'name':'name1111'}
# print(d.get('name1'))

# def my_abs(x):
# 	if x>=0:
# 		return x
# 	else:
# 		return -x

# print(my_abs(-100))

# print(my_abs(100))

# from abstest import my_abs
# v =my_abs('a')
# print(v)

# def nop():
# 	pass

# def nop():
# 	print('hahah')
# print(nop())
# print(nop())
# nop()

# import math

# def move(x,y,step,angle=0):
# 	nx=x+step*math.cos(angle)
# 	ny=y-step*math.sin(angle)
# 	return nx,ny
# # x,y=move(100,100,60,math.pi/6)

# # print(x,y)

# i=move(100,100,60,math.pi/6)
# print(i)

# from abstest import quadratic

# q=quadratic(1,2,3)
# print(q)

# def add_end(L=[]):
# 	L.append('End')
# 	return L

# # s=add_end([1,2,'3',4])
# print(add_end())

# def calc(*numbers):
# 	sum=0
# 	for n in numbers:
# 		sum = sum+n*n
# 	return sum

# print(calc(1,2,3,4,5))

# num =[2,4,5]
# print(calc(*num))

# def person(name,age,**kw):
# 	print('name:',name,'age:',age,'other:',kw)

# person('Micheal',30)
# person('Bob',35,city='BeiJing',job='Engineer')
# person('Daniel',30,city='BeiJing')

# def person (name,age,*,city='ShangHai',job):
# 	print(name,age,city,job)
# def person(name,age):
# 	print(name,age)
# def person(*char):
# 	for c in char:
# 		if isinstance(c,(int,float)):
# 			print(c)

# person('aaa',10)

# def product(*numbers):
# 	if len(numbers)==0:
# 		raise TypeError('参数有误')
# 	if len(numbers)<=1:
# 		return numbers

# 	total=1
# 	for n in numbers:
# 		if isinstance(n,(int,float)):
# 			total*=n
# 	return total

# m=product(1,2,3,10)
# print(m)

# def fact (n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)

# print(fact(5))

# L=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[1:6])
# print(L[-2:])

# L=list(range(100))
# # print(L)
# print(L[::5])

# s = '    ABCDEFGHIJKLMN    '

# print(s[-5:])
# print(s[::5])


# def trim(ss):
#     s = 0
#     for c in ss: 
#         if c != ' ':
#         	break
#         s+=1 
#     rStr = ss[s:len(ss)]

#     return rStr

# # print(trim(s))
# print(trim('hello  ')) 


# d={'a':1,'b':2,'c':3}
# # for key in d:
# # 	print(key)
# # for v in d.values():
# # 	print(v)
# for k,v in d.items():
# 	print(k,v)

# from collections  import Iterable
# isinstance('abc',Iterable)
# isinstance([1,2,3],Iterable)
# isinstance(123,Iterable)

# def findMinAndMax(L):
# 	if L==[]:
# 		return (None,None)
# 	if len(L)==1:
# 		return (L[0],L[0])
# 	min=100000000000
# 	max=0
# 	for v in L:
# 		if min>v:
# 			min=v
# 		if max<v:
# 			max=v

# 	return (min,max)

# # 测试
# if findMinAndMax([]) != (None, None):
#     print('1测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('2测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('3测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('4测试失败!')
# else:
#     print('测试成功!')

# print(list(range(1,11)))
# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2==0])
# print([m+n for m in 'ABC' for n in 'XYZ'])

# ------------------------列出文件目录---------------------------------
# import os 
# print([d for d in os.listdir('../../../')])

# d={'x':'A','y':'B','z':'C'}
# print([k+'='+v for k,v in d.items()])

# ------------------------列表生成式---------------------------------
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([l.lower() for l in L])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2=[i.lower() for i in L1 if not isinstance(i,(int,float)) if i!=None]
# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# ------------------------生成器---------------------------------
# g=(x*x for x in range(10))
# print(g)

# for n in g:
# 	print(n)

# def fib(max):
# 	n,a,b=0,0,1
# 	while n<max:
# 		print(b)
# 		a,b=b,a+b
# 		n=n+1
# 	return 'done'
# print(fib(6))

# def odd():
# 	print('step 1')
# 	yield 1
# 	print('step 2')
# 	yield 2
# 	print('step 3')
# 	yield 5

# for n in odd():
# 	print(n)
# L = [1,2]
# L2= [0,*L,0]
# print(L2)

# 杨辉三角
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L2 = [0, *L, 0]
#         L = [L2[i] + L2[i + 1] for i in range(len(L2) - 1)]

# n = 0
# results = []
# for t in triangles():
# 	print(t)
# 	results.append(t)
# 	n+=1
# 	if n==10:
# 		break;
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

