import functools

int2= functools.partial(int,base=2)

print(int2('1100'))
print(int2('10',base=10))

max2 = functools.partial(max,10)

print(max2(11,5,1,6))