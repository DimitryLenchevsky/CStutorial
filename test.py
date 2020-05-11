def conclusion_person():
    for key, value in person.items():
        print(key, ",", value)


choice = None

person = {}

while choice != 1:

    print("\t1. Выход \n\
    2. Add contact \n\
    3. Replace contact \n")

    choice = int(input("\tYour choice: \n"))

    if choice == 1:
        exit()

    elif choice == 2 or 3:
        try:
            conclusion_person()
            print()
            key = input("Введите ФИО: ")
            weight = int(input("Введите массу тела в килограммах: "))
            height = int(input("Введите Ваш рост в сантиметрах: "))
            sex = input("Введите Ваш пол: ")
            age = int(input("Введите Ваш возраст: "))
            value = [weight, height, sex, age]
            person[key] = value
            conclusion_person()
            print()
            bmi = weight / (height * height / 10000)

            print("Индекс Вашей массы тела равен: ", bmi)
            if bmi <= 16:                                    
                print("Выраженный дефицит массы тела, больше кушайте!")
            elif bmi <= 18.5:
                print("Недостаточная (дефицит) масса тела. Больше кушайте!")
            elif bmi <= 25:
                print("Ваш индекс массы тела в норме")
            elif bmi <= 30:
                print("Избыточная масса тела (предожирение), постарайтесь больше двигаться!")
            elif bmi <= 35:
                print("Ожирение, постарайтесь больше двигаться и меньше есть!")
            elif bmi <= 40:
                print("Ожирение резкое, срочно сходите к врачу!")
            elif bmi > 40:
                print("Очень резкое ожирение, срочно сходите к врачу!")
            pass

            tick = "|"
            first = bmi - 10
            second = 50 - bmi

            scale = '10' + "=" * int(first) + tick + "=" * int(second) + "50"
            print(scale)
        except Exception:
            print("O-o-ops, something went wrong")

print("Полный список пользователей: ")
print(person)