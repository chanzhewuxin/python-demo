import json 

numbers= [2,3,5,7,11,13]
filename= 'numbers.json'
with open(filename,'w',encoding='utf-8') as fs_obj:
    json.dump(numbers,fs_obj)