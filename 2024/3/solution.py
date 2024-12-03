import re


def solve_part_one(data: str) -> int:
    total = 0
    multiplies = re.findall(r'mul\([0-9]+,[0-9]+\)', data)
    for multipy in multiplies:
        multipy = multipy[4:-1]
        x, y = map(int, multipy.split(','))
        total += (x * y)
    return total


def solve_part_two(data: str) -> int:
    total = 0
    multiplies = re.finditer(r'mul\([0-9]+,[0-9]+\)', data)
    do = [item.end() for item in re.finditer(r'do\(\)', data)]
    dont = [item.end() for item in re.finditer(r'don\'t\(\)', data)]
    for multipy in multiplies:
        match = multipy.group()[4:-1]
        x, y = map(int, match.split(','))
        closest_do = max([index for index in do if index < multipy.end()], default=0)
        closest_dont = max([index for index in dont if index < multipy.end()], default=-1)
        if closest_do > closest_dont:
            total += (x * y)
    return total


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read()
    print(f'Solution 2024.3.1: {solve_part_one(data)}')
    print(f'Solution 2024.3.2: {solve_part_two(data)}')