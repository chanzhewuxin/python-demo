
# #  第一个版本
# def log(func):
# 	def wrapper(*agrs,**kw):
# 		print('call %s():'% func.__name__)
# 		return func(*agrs,**kw)
# 	return wrapper

def log(text):
	def decorator(func):
		def wrapper(*agrs,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*agrs,**kw)
		return wrapper
	return decorator

@log('你好，我只是一个日志记录')
def now():
	print('2015-4-25')

f=now()
print(now.__name__)
