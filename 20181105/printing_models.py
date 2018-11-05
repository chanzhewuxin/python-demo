# import greeter 
from greeter import greet_user

greet_user('haodongxi');

def make_pizza(*toppings):
    print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')


def build_profile(first,last ,**user_info):
    profile={}
    profile['first_name'] = first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

# user_profile= build_profile('albert','einstein',location='princeton',field='physics')
# # user_profile= build_profile('albert','einstein','princeton')
# print(user_profile)

