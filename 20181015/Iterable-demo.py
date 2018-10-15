# from collections import Iterable

# print(isinstance([],Interable))

# def f(x):
# 	return x*x

# r=map(f,[1,2,3,4,5,6,7,8,9])
# r1 = map (f,list(range(1,10)))
# print(list(r))
# print (list(r1))

# print(list(map(str,list(range(1,10)))))

# from functools import reduce
# def add(x,y):
# 	return x+y
# # print (reduce(add,[1,3,5,7,9]))
# print( [x for x in list(range(1,10)) if x%2!=0])

# def count():
# 	def f(j):
# 		def g():
# 			return j*j
# 		return g
# 	fs=[]
# 	for i in range(1,4):
# 		fs.append(f(i))
# 	return fs

# f1,f2,f3=count()
# print(f1(),f2(),f3())

