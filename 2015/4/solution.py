import hashlib


def solve_part_one(data: str):
    secret_key = 0
    while True:
        md5_hash = hashlib.md5(f'{data}{secret_key}'.encode('utf-8')).hexdigest()
        if md5_hash.startswith('00000'):
            break
        secret_key += 1
    return secret_key


def solve_part_two(data: str):
    secret_key = 0
    while True:
        md5_hash = hashlib.md5(f'{data}{secret_key}'.encode('utf-8')).hexdigest()
        if md5_hash.startswith('000000'):
            break
        secret_key += 1
    return secret_key


if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read().strip()
    print(f'Solution 2015.4.1: {solve_part_one(data)}')
    print(f'Solution 2015.4.2: {solve_part_two(data)}')
