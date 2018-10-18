from datetime import datetime,timedelta


'''
datetime demo
'''

# now = datetime.now()
# print(now)
# print(type(now))

# dt = datetime(2015,4,19,12,20)
# print(dt.timestamp())
# t =1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))

# cday  = datetime.strptime('2018-10-18 14:03:54','%Y-%m-%d %H:%M:%S')
# print(cday)

# now = datetime.now()
# print(now.strftime('%a,%b %d %H:%M'))

now = datetime.now()
print(now)
print(now+timedelta(hours=10))
