from itertools import product


def solve_part_one(data: list[str]) -> int:
    total = 0
    for line in data:
        answer, line = line.split(': ')
        answer = int(answer)
        line = list(map(int, line.split()))
        for evaluations in product(['+', '*'], repeat=len(line) - 1):
            current_total = line[0]
            for index, evaluate in enumerate(evaluations):
                if evaluate == '+':
                    current_total = (current_total + line[index + 1])
                else:
                    current_total = (current_total * line[index + 1])
            if current_total == answer:
                total += answer
                break
    return total


def solve_part_two(data: list[str]) -> int:
    total = 0
    for line in data:
        answer, line = line.split(': ')
        answer = int(answer)
        line = list(map(int, line.split()))
        for evaluations in product(['+', '*', '||'], repeat=len(line) - 1):
            current_total = line[0]
            for index, evaluate in enumerate(evaluations):
                if evaluate == '+':
                    current_total = (current_total + line[index + 1])
                elif evaluate == '||':
                    current_total = int(str(current_total) + str(line[index + 1]))
                else:
                    current_total = (current_total * line[index + 1])
            if current_total == answer:
                total += answer
                break
    return total


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    print(f'Solution 2024.7.1: {solve_part_one(data)}')
    print(f'Solution 2024.7.2: {solve_part_two(data)}')