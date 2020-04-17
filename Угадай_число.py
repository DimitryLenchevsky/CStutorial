import random
number = random.randint(1, 10)
attempt = 0
print("Компьютер загадал некоторое число. Попробуйте угадать его!")

while attempt < 10:
    print("Введите число, попробоуйте угадать его!")
    guess = input()
    guess = int(guess)

    attempt = attempt + 1

    if guess < number:
        print("Загаданное число больше твоего") 
    if guess > number:
        print("Загаданное число меньше твоего")
    if guess == number:
        break
    
if guess == number:
    attempt = str(attempt)
    print("Поздравляем, вы угадали число с "+attempt+" попытки.")
