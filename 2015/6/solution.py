def solve_part_one(data: list[str]) -> int:
    lights = set()
    for instruction in data:
        instructions = []
        instruction, xy, _, xy2 = instruction.split()[-4:]
        x, y = map(int, xy.split(','))
        x2, y2 = map(int, xy2.split(','))
        for i in range(x, x2 + 1):
            for j in range(y, y2 + 1):
                instructions.append((i, j))
        if instruction == 'on':
            for light in instructions:
                lights.add(light)
        elif instruction == 'off':
            for light in instructions:
                lights.discard(light)
        elif instruction == 'toggle':
            for light in instructions:
                if light in lights:
                    lights.remove(light)
                else:
                    lights.add(light)
    return len(lights)


def solve_part_two(data: list[str]) -> int:
    lights = {}
    for instruction in data:
        instructions = set()
        instruction, xy, _, xy2 = instruction.split()[-4:]
        x, y = map(int, xy.split(','))
        x2, y2 = map(int, xy2.split(','))
        for i in range(x, x2 + 1):
            for j in range(y, y2 + 1):
                instructions.add((i, j))
        if instruction == 'on':
            brightness = 1
        elif instruction == 'off':
            brightness = -1
        else:
            brightness = 2
        for light in instructions:
            lights[light] = max(lights.get(light, 0) + brightness, 0)
    return sum(lights.values())


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    print(f'Solution 2015.6.1: {solve_part_one(data)}')
    print(f'Solution 2015.6.2: {solve_part_two(data)}')