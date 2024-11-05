import unittest

from solution import solve_part_one, solve_part_two

class TestAdventSolution(unittest.TestCase):
    part_one = {
        0: ['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'],
        2: ['ugknbfddgicrmopn', 'aaa']
    }
    part_two = {
        0: ['uurcxstgmygtbstg', 'ieodomkazucvgmuy'],
        2: ['qjhvhtzxzqqjkmpb', 'xxyxx']
    }

    def test_part_one(self):
        for key, value in self.part_one.items():
            self.assertEqual(key, solve_part_one(value))

    def test_part_two(self):
        for key, value in self.part_two.items():
            self.assertEqual(key, solve_part_two(value))


if __name__ == '__main__':
    unittest.main()
