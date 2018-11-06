import json 

filename='numbers.json'
with open(filename,'r') as fs_obj:
    numbers= json.load(fs_obj)

print(numbers)