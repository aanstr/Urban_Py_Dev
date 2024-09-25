from time import sleep
from hashlib import sha256


class UrTube:
    """
    Класс видео, содержащий атрибуты: список пользователей,
    список видео, текущий пользователь;
    методы: логин, регистрация, логаут, добавление видео, поиск видео,
    просмотр видео
    """

    class User:
        """
        Класс пользователя, содержащий атрибуты: логин, возраст, пароль в хешированном виде
        """

        def __init__(self, nickname, age, password):
            self.nickname = nickname
            self.age = age
            self.password = sha256(password.encode()).hexdigest()  # hash

    class Video:
        """
        Класс видео, содержащий атрибуты: заголовок, продолжительность,
        секунда остановки и триггер ограничения по возрасту
        """

        def __init__(self, title, duration, time_now=0, adult_mode=False):
            self.title = title
            self.duration = duration
            self.time_now = time_now  # для возможности досмотреть начатое видео
            self.adult_mode = adult_mode

    users = {}
    videos = ()

    def __init__(self, users, videos, current_user=None):
        self.users = users
        self.duration = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        hashed_pwd = sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_pwd:
                self.current_user = user
                print(f'Добро пожаловать, {nickname}')  # тест на логин
                return

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = (nickname, password, age)
            self.users.append(user)
            self.current_user = user

    def logout(self):
        self.current_user = None


# Код для проверки:

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
