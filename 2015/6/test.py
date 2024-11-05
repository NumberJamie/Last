import unittest

from solution import solve_part_two

class TestAdventSolution(unittest.TestCase):
    part_two = {
        1: ['turn on 0,0 through 0,0'],
        2000000: ['toggle 0,0 through 999,999']
    }

    def test_part_two(self):
        for key, value in self.part_two.items():
            self.assertEqual(key, solve_part_two(value))


if __name__ == '__main__':
    unittest.main()
