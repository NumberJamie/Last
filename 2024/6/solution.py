def solve_part_one(data: list[str]) -> int:
    x, y = 0, 0
    visited = set()
    for index, line in enumerate(data):
        position = line.find('^')
        if position >= 0:
            x, y = position, index
            break
    visited.add((y, x))
    facing = 0
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    while True:
        x2, y2 = x + directions[facing][0], y + directions[facing][1]
        if x2 < 0 or x2 >= len(data[0]) or y2 < 0 or y2 >= len(data):
            break
        if data[y2][x2] == '#':
            facing = (facing + 1) % 4
            continue
        x, y = x2, y2
        visited.add((y2, x2))
    return len(visited)


def solve_part_two(data: list[str]) -> int:
    total = 0
    x, y = 0, 0
    for index, line in enumerate(data):
        position = line.find('^')
        if position >= 0:
            x, y = position, index
            break
    original_pos = (x, y)
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    for row in range(len(data)):
        for col in range(len(data[0])):
            facing = 0
            visited = set()
            obstacle = (row, col)
            x, y = original_pos
            if data[col][row] == '#' or obstacle == original_pos:
                continue
            while True:
                x2, y2 = x + directions[facing][0], y + directions[facing][1]
                if x2 < 0 or x2 >= len(data[0]) or y2 < 0 or y2 >= len(data):
                    break
                if data[y2][x2] == '#' or (x2, y2) == obstacle:
                    facing = (facing + 1) % 4
                    continue
                x, y = x2, y2
                if (x, y, facing) in visited:
                    total += 1
                    break
                visited.add((x, y, facing))
    return total


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    print(f'Solution 2024.6.1: {solve_part_one(data)}')
    print(f'Solution 2024.6.2: {solve_part_two(data)}')