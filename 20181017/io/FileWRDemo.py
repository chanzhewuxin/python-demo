# f = open('c:/GitHub/python-demo/20181017/io/test.txt','r')
# print(f.read() )
# f.close()

with open('c:/GitHub/python-demo/20181017/io/test.txt','r',encoding='utf-8',errors='ignore') as f:
    print(f.read()) 


# with open('c:/GitHub/python-demo/20181017/io/test.txt','a',encoding='utf-8',errors='ignore') as f:
#     print(f.write('写入一条记录')) 

# with open('c:/GitHub/python-demo/20181017/io/1.png','rb') as f:
#     print(f.read())