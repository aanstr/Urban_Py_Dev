import threading, time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        counter = 0
        warriors = 100
        print(f'{self.name}, на нас напали!')
        while warriors:
            counter += 1
            warriors = warriors - self.power
            print(f'{self.name} сражается {counter} дней, осталось {warriors} воинов')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
