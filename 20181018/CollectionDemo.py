from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

# Point = namedtuple('Point',['x','y'])
# p=Point(1,2)
# print(p.x,p.y)

# q= deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# q.pop()
# print(q)
# q.popleft()
# print(q)

# dd = defaultdict(lambda:'N/A')
# dd['k1'] = 'abc'
# print(dd['k1'])
# print(dd['k2'])
# print(dd)

# d = dict([('a',1),('b',2),('c',3)])
# print(d)

# od = OrderedDict([('a',1),('b',2),('c',3)])
# print(od)

c =Counter() 
for s in 'dksslfgihh,vdkada.fdsawetyu':
    c[s]= c[s]+1 

print(c) 

