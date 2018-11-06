# with open ('20181106/pi_digits.txt') as file_object:
#     contents= file_object.read()
#     print(contents.rstrip()) 


filename= '20181106/pi_digits.txt'
with open(filename) as file_object:
    # for line in file_object:
    #     print(line.rstrip())

    lines = file_object.readlines()
    print(lines)
    for line in lines:
        print(line.rstrip())