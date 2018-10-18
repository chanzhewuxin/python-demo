import re

s= r'ABC\-001'

# print(re.match(r'^\d{3}\-\d{3,8}$','010-123456'))
# print(re.match(r'^\d{3}\-\d{3,8}$','010 123456'))

# print(re.split(r'[\s\,;]+','a, b  ;c;d'))

# print(re.match(r'^(\d+)(0*)$','102300').groups())
# print(re.match(r'^(\d+?)(0*)$','102300').groups())

# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# print( re_telephone.match('010-1234456').groups())

# print(re.match(r'^[\w]+@[\w\d]+\.[\w)]+$','gel@16q.com'))

def is_valid_email(addr):
    return re.match(r'^[\w\.]+@[\w\d]+\.[\w)]+$',addr)

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
