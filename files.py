file = open("text.txt")
for line in file:
    line = str(file.readline())
    select = line.rsplit(' ')[-1]
    s_sel = select.split('/')[0]

print(select)
print(s_sel)