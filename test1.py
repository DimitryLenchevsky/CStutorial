def power(x, y=2):
    r = 1
    while y > 0:
        r = r * x
        y = y - 1
    return r

first = power(3)
print(first)

second = power(3, 3)
print(second)


def maxinum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum


result = maxinum(2, 5, 7, -1, 9, 4)
print(result)


def example_fun(x, y, **other):
    print('x: {0}, y: {1}, keys in "other": {2}'.format(x, y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]
    print('The total of values in "other" is {0}'.format(other_total))


result1 = example_fun(2, y='1', foo=3, bar=4)
print(result1)


def reverse(*args):
    for i in reversed(args):
        print(i)

b = reverse(3, 5, 6, 7, 1, 9, 6, 2)