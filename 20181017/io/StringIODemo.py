# from io import StringIO

# f=StringIO()
# f.write('hello,')
# f.write(' ')
# f.write('python')
# print(f.getvalue())

from io import BytesIO

f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f1=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f1.read())