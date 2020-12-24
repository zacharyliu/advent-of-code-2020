'''
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?
'''

from collections import defaultdict

directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']


def run():
    instructions = []
    with open('./input.txt') as f:
        for l in f.readlines():
            l = l.strip()
            instructions.append(l)
    grid = set()

    for instruction in instructions:
        flip(grid, instruction)

    for day in range(100):
        day = day + 1

        counts = defaultdict(int)
        for cur in grid:
            for direction in directions:
                counts[get(cur, direction)] += 1

        orig = set(grid)

        for cur in orig:
            if counts[cur] == 0 or counts[cur] > 2:
                grid.remove(cur)

        for cur, count in counts.items():
            if cur not in orig and count == 2:
                grid.add(cur)

        print(day, len(grid))

    return len(grid)


def flip(grid, instruction):
    cur = (0, 0)
    while instruction:
        if instruction.startswith('e'):
            cur = (cur[0] + 1, cur[1])
            instruction = instruction[1:]
        elif instruction.startswith('se'):
            cur = (cur[0], cur[1] + 1)
            instruction = instruction[2:]
        elif instruction.startswith('sw'):
            cur = (cur[0] - 1, cur[1] + 1)
            instruction = instruction[2:]
        elif instruction.startswith('w'):
            cur = (cur[0] - 1, cur[1])
            instruction = instruction[1:]
        elif instruction.startswith('nw'):
            cur = (cur[0], cur[1] - 1)
            instruction = instruction[2:]
        elif instruction.startswith('ne'):
            cur = (cur[0] + 1, cur[1] - 1)
            instruction = instruction[2:]
        else:
            raise Exception()
    if cur in grid:
        grid.remove(cur)
    else:
        grid.add(cur)


def get(cur, instruction):
    if instruction == 'e':
        cur = (cur[0] + 1, cur[1])
    elif instruction == 'se':
        cur = (cur[0], cur[1] + 1)
    elif instruction == 'sw':
        cur = (cur[0] - 1, cur[1] + 1)
    elif instruction == 'w':
        cur = (cur[0] - 1, cur[1])
    elif instruction == 'nw':
        cur = (cur[0], cur[1] - 1)
    elif instruction == 'ne':
        cur = (cur[0] + 1, cur[1] - 1)
    else:
        raise Exception()
    return cur


print(run())
