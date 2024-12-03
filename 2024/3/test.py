import unittest

from solution import solve_part_one, solve_part_two


class TestAdventSolution(unittest.TestCase):
    input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    input2 = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

    def test_part_one(self):
        self.assertEqual(solve_part_one(self.input), 161)

    def test_part_two(self):
        self.assertEqual(solve_part_two(self.input2), 48)


if __name__ == '__main__':
    unittest.main()
