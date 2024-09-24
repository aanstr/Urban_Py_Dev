from time import sleep


class UrTube:
    """
    Класс видео, содержащий атрибуты: список пользователей,
    список видео, текущий пользователь;
    методы: логин, регистрация, логаут, добавление видео, поиск видео,
    просмотр видео
    """

    class User:
        """
        Класс пользователя, содержащий атрибуты: логин, возраст, пароль
        """

        def __init__(self, nickname, age, password, password_confirm):
            self.username = nickname
            self.age = age
            if password == password_confirm:
                self.password = password  # hash

    class Video:
        """
        Класс видео, содержащий атрибуты: заголовок, продолжительность,
        секунда остановки и триггер ограничения по возрасту
        """

        def __init__(self, title, duration, time_now=0, adult_mode=False):
            self.title = title
            self.duration = duration
            self.time_now = time_now
            self.adult_mode = adult_mode

    users = {}
    videos = {}

    def __init__(self, users, videos, current_user):
        self.title = users
        self.duration = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        if password in UrTube.users:
            UrTube.current_user = nickname
            print(f'Добро пожаловать, {nickname}')
