'''
操作迭代对象的函数
'''

import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)

# l = itertools.chain('ABC','XYZ')
# print(l)
# for c in itertools.chain('ABC','XYZ'):
#     print(c)

# for key,group in itertools.groupby('AAABBCCAAAAA'):
#     print(key,list(group))

for key,group in itertools.groupby('AaaABBbbCAaaA',lambda c:c.upper()):
    print(key,list(group))