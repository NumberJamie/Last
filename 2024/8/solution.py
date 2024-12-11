from itertools import combinations


def solve_part_one(data: list[str]) -> int:
    antennas, anti_nodes = {}, set()
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '.':
                continue
            antennas.setdefault(col, []).append((x, y))
    for antenna in antennas.keys():
        for x, y in combinations(antennas[antenna], 2):
            distance = (x[0] - y[0], x[1] - y[1])
            nodes = [(x[0] + distance[0], x[1] + distance[1]), (y[0] - distance[0], y[1] - distance[1])]
            for node in nodes:
                if node[0] < 0 or node[0] >= len(data[0]) or node[1] < 0 or node[1] >= len(data[0]):
                    continue
                anti_nodes.add(node)
    return len(anti_nodes)


def solve_part_two(data: list[str]) -> int:
    antennas, anti_nodes = {}, set()
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '.':
                continue
            antennas.setdefault(col, []).append((x, y))
    for antenna in antennas.keys():
        for x, y in combinations(antennas[antenna], 2):
            distance = (x[0] - y[0], x[1] - y[1])
            for pos, direction in [(x, distance), (y, (-distance[0], -distance[1]))]:
                curr_pos = pos
                anti_nodes.add(pos)
                while True:
                    next_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
                    if not (-1 < next_pos[0] < len(data[0]) and -1 < next_pos[1] < len(data)):
                        break
                    anti_nodes.add(next_pos)
                    curr_pos = next_pos
    return len(anti_nodes)


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    print(f'Solution 2024.8.1: {solve_part_one(data)}')
    print(f'Solution 2024.8.2: {solve_part_two(data)}')