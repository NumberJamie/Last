def solve_part_one(data: list[str]) -> int:
    total = 0
    target = 'XMAS'
    rows, cols = len(data[0]), len(data)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for col in range(cols):
        for row in range(rows):
            for direction in directions:
                is_xmas = True
                x, y = direction
                for index, char in enumerate(target):
                    x_pos = col + index * x
                    y_pos = row + index * y
                    if not (0 <= x_pos < cols and 0 <= y_pos < rows):
                        is_xmas = False
                        break
                    if data[x_pos][y_pos] != char:
                        is_xmas = False
                        break
                total += 1 if is_xmas else 0
    return total


def solve_part_two(data: list[str]) -> int:
    total = 0
    target = ('MSAMS', 'MMASS', 'SMASM', 'SSAMM')
    rows, cols = len(data[0]) - 2, len(data) - 2
    for col in range(cols):
        for row in range(rows):
            matrix = ''.join(line[row:row + 3] for line in data[col:col + 3])
            modulus = ''.join(matrix[index] for index in range(len(matrix)) if index % 2 == 0)
            if modulus in target:
                total += 1
    return total


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    print(f'Solution 2024.4.1: {solve_part_one(data)}')
    print(f'Solution 2024.4.2: {solve_part_two(data)}')