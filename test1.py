x = {'a':1, 'b':2, 'c':3, 'd':4}
y = {'a':5, 'e':5, 'f':6}

del x['d']
print(x)
x.setdefault('g', 7)
print(x)
x.update(y)
print(x)
print(x.get('h', 7))
print(x)
x.setdefault('h', 7)
print(x)
print(x.items())
print(x.keys())
print(x.values())