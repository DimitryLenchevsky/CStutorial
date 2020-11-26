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