def conclusion_address_book():  # Выводит ключи и значения словаря
    for key, value in address_book.items():
        print(key, ",", value)


def write_to_file():  # Записывает данные из словаря в файл
    with open("address_book.txt", 'w', encoding="utf-8") as f:
        for key, value in address_book.items():
            f.write("{} : {}\n".format(key, value))


choice = None  # Выбор человека

address_book = {}

while choice != 1:

    print("\t1. Exit \n\
    2. Delete contact \n\
    3. Add contact \n\
    4. Replace contact \n")

    choice = int(input("\tYour choice: \n"))

    if choice == 1:
        exit()

    elif choice == 2:
        try:
            conclusion_address_book()
            print()
            delete_value_from_dict = input("Who do you want to remove?(Enter name): ")
            del address_book[delete_value_from_dict]  # Удаляет значения и ключи из словаря
            conclusion_address_book()
            print()
            print(address_book)
        except Exception:
            print("O-o-ops, something went wrong")

    elif choice == 3 or 4:
        try:
            conclusion_address_book()
            print()
            key = input("Enter name: ")
            value = input("Enter address: ")
            address_book[key] = value
            conclusion_address_book()
            print()
            write_to_file()
        except Exception:
            print("O-o-ops, something went wrong")

print(address_book)