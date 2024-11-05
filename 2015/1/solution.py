def solve_part_one(data: str) -> int:
    floor = 0
    for char in data:
        floor += 1 if char == '(' else -1
    return floor


def solve_part_two(data: str) -> int:
    floor = 0
    for index, char in enumerate(data):
        floor += 1 if char == '(' else -1
        if floor < 0:
            break
    return index + 1


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read().strip()
    print(f'Solution 2015.1.1: {solve_part_one(data)}')
    print(f'Solution 2015.1.2: {solve_part_two(data)}')
