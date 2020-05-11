def draw_menu():
    pass
def do_one():
    pass
users = {}
def do_two():
    pass
def ask_option():
    # что-то
    return 'some answer'
def do_else():
    pass
def draw_scale(bmi):
    print('30*********37*********40')
def get_user_data():
    # TODO: request user data
    # 
    return {'name': 'Ivan', 'age': 100}
def save_user(user):
    # {'name'}
    global users
    users[uuid.uuid4(): user]
    # TODO выбрать как сохранять (в память, на диск)
    return True
def get_user_to_delete():
    #  input
    # search
    # user_id 'dsdfsdfgfsdsgergeswrtgfer'
    return 'dsdfsdfgfsdsgergeswrtgfer' # user_id

def delete_user(user_id):
    global users
    users.pop(user_id, None)
def qui():
    pass

def process_answer(answer):
    if answer == 1:
        user = get_user_data()
        save_user(user)
    elif answer == 2:
        # delete
        user_id = get_user_to_delete()
        delete_user(user_id)
            
    elif answer == 'q':
        qui()
        draw_scale()
        draw_scale()
    else:
        draw_menu()
        answer = ask_option()
        if answer == 'в':
            print('пока')
            break

def main():
    while True:
        draw_menu()
        answer = ask_option()
        if answer == 'в':
            print('пока')
            break
        process_answer(answer)















































if __name__ == "__main__":
    main()