import unittest
import tests_12_3 as test

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
