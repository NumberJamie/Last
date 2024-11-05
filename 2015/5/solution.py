def solve_part_one(data: list[str]) -> int:
    vowels = set('aeiou')
    forbidden = {'ab', 'cd', 'pq', 'xy'}
    valid_texts = 0
    for text in data:
        if not sum(1 for char in text if char in vowels) >= 3:
            continue
        if not any(text[i] == text[i + 1] for i in range(len(text) - 1)):
            continue
        if not all(text[i:i + 2] not in forbidden for i in range(len(text) - 1)):
            continue
        valid_texts += 1
    return valid_texts


def solve_part_two(data: list[str]) -> int:
    valid_texts = 0
    for text in data:
        if not any(text[i] == text[i + 2] for i in range(len(text) - 2)):
            continue
        pairs = []
        for index in range(len(text) - 1):
            pair = text[index:index + 2]
            if pair in pairs[:-1]:
                valid_texts += 1
                break
            pairs.append(pair)
    return valid_texts


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readlines()
    print(f'Solution 2015.5.1: {solve_part_one(data)}')
    print(f'Solution 2015.5.2: {solve_part_two(data)}')
