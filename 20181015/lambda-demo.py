print(list(map(lambda x: x*x ,list(range(1,10)))))

f = lambda x: x*x;
print(f(4))

def build (x,y):
	return lambda: x*x+y*y

print(build(2,4)())

# L=list(filter(lambda: x%2==1,range(1,20)))
# print(L)

def is_odd(n):
	return n%2==1

L= list(filter(is_odd,range(1,20)))
print(L)

K = list(filter(lambda x:x%2==1,range(1,20)))
print(K)