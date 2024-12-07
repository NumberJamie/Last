import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    input = ['....#.....', '.........#', '..........', '..#.......',  '.......#..', '..........', '.#..^.....',
             '........#.', '#.........', '......#...']

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 41)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input), 6)


if __name__ == '__main__':
    unittest.main()
