import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    input = ['190: 10 19', '3267: 81 40 27', '83: 17 5', '156: 15 6', '7290: 6 8 6 15', '161011: 16 10 13',
             '192: 17 8 14', '21037: 9 7 18 13', '292: 11 6 16 20',]

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 3749)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input), 11387)


if __name__ == '__main__':
    unittest.main()
