import random

def pass_gen(min_length=5):
    a = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4']
    password_list = []
    random.shuffle(a)
    password_list = ''.join([random.choice(a) for x in range(min_length)])
    return password_list

pwd = pass_gen(min_length=5)
print(pwd)

dict = {}
dict[1] = pwd

print(dict)