def my_gen():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1
for i in my_gen():
    print(i)
