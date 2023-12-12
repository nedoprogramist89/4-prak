import tables
import datetime
from classes import *
from tables import *

if __name__ == "__main__":
    database = Database()
    auth_system = AuthSystem(database)

    currect_acc = 0
    firstTime = False

    #Создание таблиц
    tables.create_visitors()
    tables.create_admin_table()
    tables.create_basket()
    tables.create_service()
    create_employees()
    # tables.auto_insert()

    while True:
        if not firstTime:
            print("""Напишите login чтобы войти в аккаунт \nНапишите register чтобы зарегистрироваться \nНапишите logout чтобы выйти из аккаунта""")
            firstTime = True
        text = input()
        if text == "login" and currect_acc == 0:
            print("Введите имя пользователя")
            username = input()
            print("Введите пароль")
            password = input()
            isAllrigh = auth_system.login(username, password)
            if isAllrigh:
                currect_acc = database.get_user_by_username(username)
                if currect_acc[3] == "visitor":
                    print("Чтобы записаться на прием напишите make request \nЧтобы отменить запись на прием напишите delete request \nЧтобы увидеть карзину напишите view basket")
                if currect_acc[3] == "admin":
                        print("Чтобы заблокировать запись на прием напишите block request \nЧтобы заблокировать пользователя напишите block user \nЧтобы посмотреть список всех пользователей напишите view users \nЧтобы увидеть карзину всех пользователей напишите view users basket")
                if currect_acc[3] == "employee":
                        print('Чтобы увидеть карзину всех пользователей напишите view users basket \nЧтобы увидеть все услуги view services \nЧтобы добавить услугу напишите add service \nЧтобы удалить услугу напишите delete service')
        elif text == "login" or text == "register" and currect_acc != 0:
            print("Вы уже находитесь в аккаунте")

        elif text == "logout" and currect_acc != 0:
            currect_acc = 0
            print("Вы успешно вышли из аккаунта")
        elif text == "logout" and  currect_acc == 0:
            currect_acc = 0
            print("Вы не нахоидтесь в аккаунте")

        elif text == "register" and currect_acc == 0:
            print("Придумайте имя пользователя")
            username = input()
            users = []
            for user in auth_system.database.users:
                users.append(user[1])
            if username in users:
                print("Такое имя пользователя уже существует")
            else:
                print("Придумайте пароль")
                password = input()
                print("Введите свой номер телефона")
                phone = input()
                print("Введите свою электронную почту")
                email = input()
                auth_system.register(username, password)
                tables.add_data(len(tables.view_users("only_users"))+1, username, password, "visitor", phone, email)

        elif text == "make request" and currect_acc != 0:
            database.make_request(currect_acc[1])

        elif text == "delete request" and currect_acc != 0:
            database.delete_request(currect_acc[1])

        elif text == "block user" and currect_acc != 0:
            database.block_user(currect_acc[1])

        elif text == "block request" and currect_acc != 0:
            database.block_request(currect_acc[1])

        elif text == "view users" and currect_acc != 0:
            database.view_users(currect_acc[1])
        elif text == "view basket" and currect_acc != 0:
            database.view_basket(currect_acc[1])
        elif text == "view users basket" and currect_acc != 0:
            database.view_users_basket(currect_acc[1])
        elif text == "add service" and currect_acc != 0:
            database.add_sevice(currect_acc[1])
        elif text == "view services" and currect_acc != 0:
            database.view_sevice(currect_acc[1])
        elif text == "delete service" and currect_acc != 0:
            database.delete_sevice(currect_acc[1])

        else:
            print("Ошибка, попробуйте еще раз")



