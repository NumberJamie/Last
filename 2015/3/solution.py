def solve_part_one(data: str) -> int:
    x, y = 0, 0
    delivered = 1
    visited = {(x, y)}
    directions = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    for char in data:
        move_x, move_y = directions[char]
        x += move_x
        y += move_y
        position = (x, y)
        if position not in visited:
            delivered += 1
            visited.add(position)
    return delivered


def solve_part_two(data: str) -> int:
    x, y = 0, 0
    x2, y2 = 0, 0
    delivered = 1
    visited = {(x, y)}
    directions = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    for index, char in enumerate(data):
        move_x, move_y = directions[char]
        if index % 2 == 0:
            x2 += move_x
            y2 += move_y
            position = (x2, y2)
        else:
            x += move_x
            y += move_y
            position = (x, y)
        if position not in visited:
            delivered += 1
            visited.add(position)
    return delivered


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read().strip()
    print(f'Solution 2015.3.1: {solve_part_one(data)}')
    print(f'Solution 2015.3.1: {solve_part_two(data)}')
