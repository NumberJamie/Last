import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    input = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS',
             'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 18)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input), 9)


if __name__ == '__main__':
    unittest.main()
