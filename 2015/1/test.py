import unittest

from solution import solve_part_one, solve_part_two

class TestAdventSolution(unittest.TestCase):
    part_one = {
        -3: [')))', ')())())'],
        -1: ['())', '))('],
        0: ['(())', '()()'],
        3: ['(((', '(()(()(', '))(((((']
    }
    part_two = {
        1: ')',
        5: '()())'
    }

    def test_part_one(self):
        for key, values in self.part_one.items():
            for value in values:
                self.assertEqual(key, solve_part_one(value))

    def test_part_two(self):
        for key, value in self.part_two.items():
            self.assertEqual(key, solve_part_two(value))


if __name__ == '__main__':
    unittest.main()
