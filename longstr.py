from datetime import datetime

# сам декоратор, который применяеться к фкнециям. а в самих функиях функционал декоратора закомментирован.
def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper    

@timeit
def one():
    #start = datetime.now()
    l = []
    for i in range(10000):
        if i % 2 == 0:
            l.append(i)
    #print(datetime.now() - start)
    return l
@timeit
def two():
    #start = datetime.now()
    l = [x for x in range(10000) if x % 2 == 0]
    #print(datetime.now() - start)
    return l

l1 = one()
l2 = two()

#print(l1)
#print(l2)