import unittest
import runner_and_tournament as run
from runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        bob = Runner('Bob')
        for _ in range(10):
            bob.walk()
        self.assertEqual(bob.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rob = Runner('Rob')
        for _ in range(10):
            rob.run()
        self.assertEqual(rob.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rob = Runner('Rob')
        bob = Runner('Bob')
        for _ in range(10):
            bob.walk()
            rob.run()
        self.assertNotEqual(bob.distance, rob.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = run.Runner('Усэйн', 10)
        self.andrey = run.Runner('Андрей', 9)
        self.nik = run.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        race = run.Tournament(90, self.usain, self.nik)
        result = race.start()
        self.all_results[0] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(max(result.keys()), 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        race = run.Tournament(90, self.andrey, self.nik)
        result = race.start()
        self.all_results[1] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(max(result.keys()), 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        race = run.Tournament(90, self.usain, self.andrey, self.nik)
        result = race.start()
        self.all_results[2] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(max(result.keys()), 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test4(self):
        race = run.Tournament(90, self.nik, self.andrey, self.usain)
        result = race.start()
        self.all_results[3] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(max(result.keys()), 'Ник')

    @classmethod
    def tearDownClass(cls):
        for race in cls.all_results:
            print(f'Забег {race+1}: {cls.all_results.__getitem__(race)}')


if __name__ == '__main__':
    unittest.main()
