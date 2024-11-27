import unittest
import runner_and_tournament as run


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = run.Runner('Усэйн', 10)
        self.andrey = run.Runner('Андрей', 9)
        self.nik = run.Runner('Ник', 3)

    def test1(self):
        race = run.Tournament(90, self.usain, self.nik)
        result = race.start()
        self.all_results.update({place: str(runner) for place, runner in result.items()})
        self.assertTrue(max(self.all_results.keys()), 'Ник')

    def test2(self):
        race = run.Tournament(90, self.andrey, self.nik)
        result = race.start()
        self.all_results.update({place: str(runner) for place, runner in result.items()})
        self.assertTrue(max(self.all_results.keys()), 'Ник')

    def test3(self):
        race = run.Tournament(90, self.usain, self.andrey, self.nik)
        result = race.start()
        self.all_results.update({place: str(runner) for place, runner in result.items()})
        self.assertTrue(max(self.all_results.keys()), 'Ник')

    def test4(self):
        race = run.Tournament(90, self.nik, self.andrey, self.usain)
        result = race.start()
        self.all_results.update({place: str(runner) for place, runner in result.items()})
        self.assertTrue(max(self.all_results.keys()), 'Ник')

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results.values())
        for race in cls.all_results:
            print(cls.all_results.__getitem__(race))


if __name__ == '__main__':
    unittest.main()
