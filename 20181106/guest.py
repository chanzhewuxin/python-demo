# # filename ='guest.txt'
# # name = input("Please input your name :")
# # with open(filename,'w') as file_object:
# #     file_object.write("Your are "+name.title()+" Welcome to you.\n" )

# count =0 
# filename = 'guest_book.txt'
# while count<5:
#     name = input("Please your name:")
#     print("欢迎您，%s " % name)
#     with open(filename,'a',encoding='utf-8') as file_obj:
#         file_obj.write("你是：%s 。\n" % name)
#     count+=1


str =' a b c d a  aaa ffda   aa a '
print(str.count('a'))