import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    ordering = {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29],
                29: [13], 53: [29, 13]}
    printable = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29],
                 [97, 13, 75, 29, 47]]

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.ordering, self.printable), 143)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.ordering, self.printable), 123)


if __name__ == '__main__':
    unittest.main()
