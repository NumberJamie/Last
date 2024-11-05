import unittest

from solution import solve_part_one

class TestAdventSolution(unittest.TestCase):
    part_one = {
        609043: 'abcdef',
        1048970: 'pqrstuv'
    }

    def test_part_one(self):
        for key, value in self.part_one.items():
            self.assertEqual(key, solve_part_one(value))


if __name__ == '__main__':
    unittest.main()
