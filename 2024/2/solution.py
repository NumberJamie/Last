def solve_part_one(data: list[str]) -> int:
    total = 0
    for line in data:
        line = list(map(int, line.split()))
        line_len = len(line) - 1
        if not all(1 <= abs(line[index] - line[index + 1]) <= 3 for index in range(line_len)):
            continue
        if all(line[index] < line[index + 1] for index in range(line_len)):
            total += 1
        elif all(line[index] > line[index + 1] for index in range(line_len)):
            total += 1
    return total


def is_valid(line: list[int]) -> bool:
    line_len = len(line) - 1
    if not all(1 <= abs(line[index] - line[index + 1]) <= 3 for index in range(line_len)):
        return False
    if (all(line[index] < line[index + 1] for index in range(line_len)) or
            all(line[index] > line[index + 1] for index in range(line_len))):
        return True
    return False


def solve_part_two(data: list[str]) -> int:
    total = 0
    for line in data:
        line = list(map(int, line.split()))
        if is_valid(line):
            total += 1
            continue
        if sum(is_valid(line[:index] + line[index + 1:]) for index in range(len(line))) >= 1:
            total += 1
    return total


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    print(sum([True, False]))
    print(f'Solution 2024.2.1: {solve_part_one(data)}')
    print(f'Solution 2024.2.2: {solve_part_two(data)}')