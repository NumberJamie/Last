import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    input = ['3 4', '4 3', '2 5', '1 3', '3 9', '3 3']

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 11)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input), 31)


if __name__ == '__main__':
    unittest.main()
