from time import sleep
from hashlib import sha256


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, возраст, пароль в хешированном виде
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = sha256(password.encode()).hexdigest()  # hash
        self.age = age


class Video:
    """
    Класс видео, содержащий атрибуты: заголовок, продолжительность,
    секунда остановки и триггер ограничения по возрасту
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now  # для возможности досмотреть начатое видео(не реализовано)
        self.adult_mode = adult_mode


class UrTube:
    """
    Класс видео, содержащий атрибуты: список пользователей,
    список видео, текущий пользователь;
    методы: логин, регистрация, логаут, добавление видео, поиск видео,
    просмотр видео
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_pwd = sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_pwd:
                self.current_user = user
                return
        print("Неверные учетные данные")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user

    def logout(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword):
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                return video.title

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    print(video.time_now)
                    sleep(1)
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0
                return

        print("Видео не найдено")


if __name__ == '__main__':
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
