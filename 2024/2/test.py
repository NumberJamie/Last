import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    input = ['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 7 9']

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 2)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input), 4)


if __name__ == '__main__':
    unittest.main()
