from collections import Counter


def solve_part_one(data: list[str]) -> int:
    left, right = [], []
    for line in data:
        left_val, right_val = map(int, line.split())
        left.append(left_val)
        right.append(right_val)
    left.sort()
    right.sort()
    count = 0
    for index in range(len(left)):
        count += abs(left[index] - right[index])
    return count


def solve_part_two(data: list[str]) -> int:
    left, right = [], []
    for line in data:
        left_val, right_val = map(int, line.split())
        left.append(left_val)
        right.append(right_val)
    count = 0
    counts = Counter(right)
    for item in left:
        count += (item * counts.get(item, 0))
    return count


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    print(f'Solution 2024.1.1: {solve_part_one(data)}')
    print(f'Solution 2024.1.2: {solve_part_two(data)}')