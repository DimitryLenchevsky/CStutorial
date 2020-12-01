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


x = 'Mississipi'
print(x.find('ss'))
print(x.find('zz'))
print(x.find('ss', 3))
print(x.find('ss', 0, 3))
print(x.index('ss'))
print(x.count('ss'))

print(x.endswith('ssipi'))
print(x.startswith('Missi'))

print(x.swapcase())
print(x.capitalize())
print(x.count('M'))
print(x.index('Miss'))



text = 'Hello, World'
wordlist = list(text)
print(wordlist)
print(list(text))
wordlist[6:] = []
wordlist.reverse()
text = "".join(wordlist)
print(text)


text = 'Hello, word, hello'
print(text.replace(',', ' '))


x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
y = ' '.join(x)
c = y.replace('"', '')
x = c.split(" ")
print(x)


x = 'Mississippi'
c = list(x)
del c[-2]
x = ' '.join(c)
print(x)
