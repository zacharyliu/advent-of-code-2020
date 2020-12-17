'''
'''

from collections import defaultdict


def run():
    nums = []
    last = defaultdict(list)
    with open('./input.txt') as f:
        i = 1
        for c in f.readline().strip().split(','):
            c = int(c)
            nums.append(c)
            last[c].append(i)
            i += 1

    while len(nums) < 30000000:
        if nums[-1] in last and len(last[nums[-1]]) > 1:
            i = last[nums[-1]][-1] - last[nums[-1]][-2]
        else:
            i = 0
        nums.append(i)
        last[i].append(len(nums))
        last[i] = last[i][-2:]

    return nums[-1]


print(run())
