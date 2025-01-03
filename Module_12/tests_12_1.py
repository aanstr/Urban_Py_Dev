import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        bob = Runner('Bob')
        for _ in range(10):
            bob.walk()
        self.assertEqual(bob.distance, 50)

    def test_run(self):
        rob = Runner('Rob')
        for _ in range(10):
            rob.run()
        self.assertEqual(rob.distance, 100)

    def test_challenge(self):
        rob = Runner('Rob')
        bob = Runner('Bob')
        for _ in range(10):
            bob.walk()
            rob.run()
        self.assertNotEqual(bob.distance, rob.distance)


if __name__ == '__main__':
    unittest.main()
