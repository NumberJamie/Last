def solve_part_one(ordering: dict[int,list[int]], printable: list[list[int]]) -> int:
    total = 0
    for line in printable:
        if all(line[index + 1] in ordering.get(line[index], []) for index in range(len(line) - 1)):
            total += line[len(line) // 2]
    return total


def solve_part_two(ordering: dict[int,list[int]], printable: list[list[int]]) -> int:
    total = 0
    for line in printable:
        if all(line[index + 1] in ordering.get(line[index], []) for index in range(len(line) - 1)):
            continue
        while not all(line[index + 1] in ordering.get(line[index], []) for index in range(len(line) - 1)):
            for index in range(len(line) - 1):
                if line[index + 1] not in ordering.get(line[index], []):
                    line[index], line[index + 1] = line[index + 1], line[index]
        total += line[len(line) // 2]
    return total


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    ordering, printable = {}, []
    is_rule = True
    for line in data:
        if not line:
            is_rule = False
        elif is_rule:
            first, second = map(int, line.split('|'))
            ordering.setdefault(first, []).append(second)
        else:
            printable.append(list(map(int, line.split(','))))
    print(f'Solution 2024.5.1: {solve_part_one(ordering, printable)}')
    print(f'Solution 2024.5.2: {solve_part_two(ordering, printable)}')