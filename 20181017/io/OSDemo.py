import os

# print(dir(os))
# print(os.name)
# print(os.get_exec_path)
# print(os.mkdir)

# print(hasattr(os, 'uname'))
# print(os.uname_result)

# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x','default'))

# print(os.path.abspath('.'))
# s,p = os.path.splitext('/path/to/file.txt')
# print(s)

# os.rename('test.txt','test.py')
# os.remove('test.txt')

print([x for x in os.listdir('.') ])
# print([x for x in os.listdir('.') if os.path.isdir(x)]) #打印当前文件夹中的文件夹名称
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
