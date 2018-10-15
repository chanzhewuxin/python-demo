import math

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x


def quadratic(a,b,c):
	# if not isinstance(a,b,c,(int,float)):
	# 	raise TypeError('bad operand type')
	x1=(-b+math.sqrt(b*b-4*a*c))/2*a
	x2=(-b-math.sqrt(b*b-4*a*c))/2*a
	return	x1,x2