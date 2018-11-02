# invitor = ['老婆','母亲','奶奶']
# print(invitor)
# print('%s 无法赴约' % invitor[2])
# invitor[2]='丈母娘'
# print(invitor)

# invitor.insert(0,'gugu')
# print (invitor)
# invitor.insert(2,'jiejie')
# print(invitor)
# invitor.append('haha')
# print(invitor)
# print('抱歉，%s 无法邀请您来共进晚餐了。' % invitor.pop())
# print('抱歉，%s 无法邀请您来共进晚餐了。' % invitor.pop())
# print('抱歉，%s 无法邀请您来共进晚餐了。' % invitor.pop())
# print('抱歉，%s 无法邀请您来共进晚餐了。' % invitor.pop())
# print(invitor)
# print('%s , 你任然在邀请之列' % invitor[0])
# print('%s , 你任然在邀请之列' % invitor[1])
# del invitor[0]
# del invitor[0]
# print(invitor)

####### 3.3.2
cars = ['bmw','Audi','toyota','audi','subaru']
numbers = [ 23,45,6.26,2367,267.23,56781]
chars=["你好",'哈哈','中文','不是吧','啊啊啊']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print(sorted(numbers))
print(sorted(chars))
print('\nHere is the origin list:')
cars.reverse()
print(cars)
print(cars[-1])