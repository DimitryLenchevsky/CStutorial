name_age = {}

for i in range(3):
    name = input('Name? ')
    age = int(input('Age? '))
    name_age[name] = age

name_choice = input('Name to find? ')
if name_choice in name_age:
    print(name_age[name_choice])
else:
    print('There is no such name in the dict')