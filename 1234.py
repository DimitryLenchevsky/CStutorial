s = input()

digits = "0123456789"

while True:
    isNumber = True
    for symbol in s:
        if symbol not in digits:
            isNumber = False
            break
        
    if isNumber:
        break
          
    print("Please input a number.")
    s = input()

n = int(s)
print(n**100)
