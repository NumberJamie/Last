def solve_part_one(data: list[str]) -> int:
    wrapping_paper = 0
    for dimensions in data:
        length, width, height = map(int, dimensions.split("x"))
        areas = [length * width, width * height, height * length]
        wrapping_paper += min(areas) + sum(areas) * 2
    return wrapping_paper


def solve_part_two(data: list[str]) -> int:
    ribbon = 0
    for dimensions in data:
        length, width, height = map(int, dimensions.split("x"))
        volume = length * width * height
        min_one, min_two, _ = sorted([length, width, height])
        ribbon += (2 * (min_one + min_two)) + volume
    return ribbon


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    print(f'Solution 2015.2.1: {solve_part_one(data)}')
    print(f'Solution 2015.2.2: {solve_part_two(data)}')
