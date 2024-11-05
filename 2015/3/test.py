import unittest

from solution import solve_part_one, solve_part_two

class TestAdventSolution(unittest.TestCase):
    part_one = {
        '>': 2,
        '^v^v^v^v^v': 2,
        '^>v<': 4
    }
    part_two = {
        '^v': 3,
        '^v^v^v^v^v': 11,
        '^>v<': 3
    }

    def test_part_one(self):
        for key, value in self.part_one.items():
            self.assertEqual(value, solve_part_one(key))

    def test_part_two(self):
        for key, value in self.part_two.items():
            self.assertEqual(value, solve_part_two(key))


if __name__ == '__main__':
    unittest.main()
