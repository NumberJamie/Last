import unittest

from solution import solve_part_one, solve_part_two

class TestAdventSolution(unittest.TestCase):
    part_one = {
        58: ['2x3x4'],
        43: ['1x1x10']
    }
    part_two = {
        34: ['2x3x4'],
        14: ['1x1x10']
    }

    def test_part_one(self):
        for key, value in self.part_one.items():
            self.assertEqual(key, solve_part_one(value))

    def test_part_two(self):
        for key, value in self.part_two.items():
            self.assertEqual(key, solve_part_two(value))


if __name__ == '__main__':
    unittest.main()
