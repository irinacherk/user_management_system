class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__access_level = access_level  # Приватный атрибут

    # Геттеры для получения данных
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттеры для изменения данных
    def set_name(self, new_name):
        self.__name = new_name

    def set_access_level(self, new_access_level):
        self.__access_level = new_access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.users = []  # Список пользователей, которым управляет администратор

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.get_user_id() != user_id]


# Пример использования
user1 = User(1, "Иван")
user2 = User(2, "Петр")
admin = Admin(0, "Админ")

admin.add_user(user1)
admin.add_user(user2)

# Демонстрация работы геттеров и сеттеров
print(admin.get_name())  # "Админ"
admin.set_name("Новый Админ")
print(admin.get_name())  # "Новый Админ"

# Удаление пользователя
admin.remove_user(1)
for user in admin.users:
    print(user.get_name())  # Выведет "Петр"
