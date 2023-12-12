import random
import tables

class Database:
    def __init__(self):
        users_ = tables.get_all_users()
        self.users = users_

    def add_user(self, user):
        self.users.append(user)

    def get_user_by_username(self, username):
        try:
            for user in tables.get_all_users():
                if user[1] == username:
                    return user
        except:
            return None

    def block_user(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "admin":
            print("Введите имя пользователя, которого хотите заблокировать")
            name = input()
            names = []
            for name_ in tables.get_all_users():
                names.append(name_[1])
            if name in names:
                tables.block_user(name)
                print(f"Пользователь {name} заблокирован")
            else:
                print("Пользователь не найден")
        else:
            print("Недостаточно прав")

    def make_request(self, username):
        baskets = tables.view_basket()
        ids = [0]
        for i in baskets:
            ids.append(i[0])

        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "visitor":
            data = tables.view_services()
            str_ = "Выберите тариф: "
            tariffs = []
            for service in data:
                str_ += f"\n{service[1]} - {service[2]}"
                tariffs.append(service[1])
            print(str_)
            tariff = input()
            if tariff in tariffs:
                for i in data:
                    if tariff == i[1]:
                        price = i[2]
                tables.make_request(max(ids)+1, username, tariff, price)
                print("Отлично заказ сделан!")
            else:
                print("Тариф не найден")
        else:
            print("Недостаточно прав")

    def delete_request(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "visitor":
            data = tables.users_basket(currect_user[1])
            if data == []:
                print("У вас нет записей")
            else:
                print("Введите id записи")
                id = input()
                ids = []
                for i in data:
                    ids.append(i[0])
                if int(id) in ids:
                    tables.delete_request(int(id))
                    print("Вы успешно отменили запись на прием!")
                else:
                    print("Такой записи не существует")
        else:
            print("Недостаточно прав")

    def block_request(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "admin":
            print("Введите имя пользователя у которого хотите заблокировать запись на прием")
            name = input()
            data = tables.users_basket(name)
            print("Введите id записи")
            id = input()
            ids = []
            names=[]
            for i in data:
                names.append(i[1])
            for j in data:
                ids.append(j[0])
            if data != [] and str(name) in names and int(id) in ids:
                tables.delete_request(int(id))
                print(f"Вы успешно заблокировали запись на прием пользователя {name}!")
            else:
                print("У этого пользователя нет заказов")
        else:
            print("Недостаточно прав")

    def view_users(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "admin":
            if tables.view_users("all_users") == []:
                print("Пользователей нету")
            else:
                for user in tables.get_all_users():
                    print(*user)
        else:
            print("Недостаточно прав")

    def view_basket(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "visitor":
            if tables.users_basket(currect_user[1]) != []:
                for text in tables.users_basket(currect_user[1]):
                    print(*text)
            else:
                print("У вас нет заказов")
        else:
            print("Недостаточно прав")

    def view_users_basket(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "employee" or currect_user[3] == "admin":
            data = tables.view_basket()
            if data == []:
                print("Корзина пуста")

            for i in data:
                print(*i)

        else:
            print("Недостаточно прав")

    def add_sevice(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "employee":
            print("Введите название услуги")
            name = input()
            print("Введите цену")
            price = input()

            data = tables.view_services()
            ids = []

            for i in data:
                ids.append(i[0])

            tables.add_service(max(ids)+1, name, price)
            print("Услуга успешно добавлена")
        else:
            print("Недостаточно прав")

    def delete_sevice(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "employee":
            print("Введите название услуги которую хотетие удалить")
            name = input()

            data = tables.view_services()
            names = []

            for i in data:
                names.append(i[1])

            if name in names:
                tables.delete_service(name)
                print("Услуга успешно удалена")
            else:
                print("Услуга не нейдена")
        else:
            print("Недостаточно прав")

    def view_sevice(self, username):
        currect_user = self.get_user_by_username(username)
        if currect_user[3] == "employee":
            data = tables.view_services()
            for i in data:
                print(*i)
        else:
            print("Недостаточно прав")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orederid = 0

class AuthSystem:
    def __init__(self, database):
        self.database = database

    def register(self, username, password):
        # Регистрация пользователя
        new_user = User(username, password)
        self.database.add_user(new_user)
        print("Регистрация успешна.")
        return self.database.get_user_by_username(username)

    def login(self, username, password):
        # Вход в аккаунт
        usernames = []
        currect_user = self.database.get_user_by_username(username)
        for users_ in tables.get_all_users():
            usernames.append(users_[1])
        if username not in usernames or password != currect_user[2]:
            print("Неправильное имя аккаунта или пароль")
            return False
        else:
            if username == currect_user[1] and password == currect_user[2]:
                print("Вы успешно вошли")
                return True
