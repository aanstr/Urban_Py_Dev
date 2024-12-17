import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s) | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Имя может быть только строкой')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError('Скорость может быть только положительной')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = Runner('Runner1', -5)
            for _ in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner2 = Runner(5, 5)
            for _ in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rob = Runner('Rob')
        bob = Runner('Bob')
        for _ in range(10):
            bob.walk()
            rob.run()
        self.assertNotEqual(bob.distance, rob.distance)
