string1 = 'a\n\tb'
print(string1)


print('abc\n')
print('abc\n', end='')


x = 'hello world!'
c = x.upper()
print(c)


t = ' '.join(['join', 'puts', 'spaces', 'between', 'elements'])
print(t)
t = '::'.join(['Separated', 'with', 'colons'])
print(t)

e = t.split('::')
print(e)

x = 'a b c d'
c = x.split(' ', 1)
print(c)
c = x.split(' ', 2)
print(c)
c = x.split(' ', 9)
print(c)


x = 'this is a test'
c = x.split(' ')
x = '-'.join(c)
print(x)

x = 'this is a test'
c = '-'.join(x.split(' '))
print(c)


x = '    Hello,    World\t\t'
print(x)
print(x.strip())
print(x.lstrip())
print(x.rstrip())


import string
print(string.whitespace)