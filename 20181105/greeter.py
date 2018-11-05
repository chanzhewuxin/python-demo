def greet_user(username):
    """显示简单的问候语"""
    print("Hello! %s" % username.title())

# greet_user("ameng")


def decribe_pet(pet_name, animal_type='dog'):
    print("\nI have a %s ." % animal_type)
    print("My "+animal_type+"'s name is " + pet_name)


# decribe_pet('hamster','harry')
# decribe_pet('dog','willie')
# decribe_pet('hony')
# decribe_pet(pet_name='name')
# decribe_pet(animal_type='cat',pet_name='宠物名称')

def make_shirt(size=None, remark='I love python.'):
    if(size != None):
        print('我有一件T恤，%s码，上面写着：%s' % (size, remark))
    else:
        print('我有一件写着：%s 的T恤' % remark)

# make_shirt('L','Superme')
# make_shirt(size='M',remark='Js do it.')
# make_shirt('大号')
# make_shirt('中号')
# make_shirt()
# make_shirt(remark='好多花纹')


def get_formatted_name(first_name, last_name, middle_name=""):
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name

# musician = get_formatted_name('john','lee','hooker')
# print(musician)


def build_person(first_name, last_name, other_proporty={}):
    person = {'first': first_name, 'last': last_name}
    for prop,val in other_proporty.items():
        person[prop]=val
    return person


# musician = build_person('jinmi', 'hendrix',{'age':20,'sex':'L'})
# print(musician)

# while input('Please your name :')!='q':
#     print('你输入的名字是：%s ' )