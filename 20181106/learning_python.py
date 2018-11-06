with open('20181106/learning_python.txt') as file_object:
    lines = file_object.readlines()
    for l in lines:
        print(l.rstrip())
        print(l.replace("Python","C").rstrip())
    # for l in file_object:
    #     print(l.rstrip())
    # print(type( file_object))