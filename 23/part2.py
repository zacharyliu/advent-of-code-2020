'''
Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the crab starts arranging many cups in a circle on your raft - one million (1000000) in total.

Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.) In this way, every number from one through one million is used exactly once.

After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. You can have them if you predict what the labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?
'''

from tqdm import trange
import math


class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


def run():
    cups = []
    with open('./input.txt') as f:
        l = f.readline().strip()
        prev = None
        for c in l:
            cup = Node(int(c), prev, None)
            if prev is not None:
                prev.next = cup
            cups.append(cup)
            prev = cup
    for i in trange(len(cups), 1_000_000):
        cup = Node(i + 1, prev, None)
        prev.next = cup
        cups.append(cup)
        prev = cup
    cups[-1].next = cups[0]
    cups[0].prev = cups[-1]

    rev = {cup.val: cup for cup in cups}

    cur = cups[0]
    min_v, max_v = min(rev.keys()), max(rev.keys())
    for _ in trange(10_000_000):
        cur = play(rev, min_v, max_v, cur)

    return label(cur)


def label(cur):
    while cur.val != 1:
        cur = cur.next
    cur = cur.next
    output = []
    for _ in range(2):
        output.append(cur.val)
        cur = cur.next
    return math.prod(output)


def play(rev, min_v, max_v, cur):
    removed = []
    next_removed = cur.next
    for _ in range(3):
        removed.append(next_removed)
        prev, next = next_removed.prev, next_removed.next
        next_removed.next.prev = prev
        next_removed.prev.next = next
        next_removed.prev = None
        next_removed.next = None
        next_removed = next
    dest = None
    search = cur.val - 1
    while dest is None:
        if search in rev and rev[search] not in removed:
            dest = rev[search]
            break
        else:
            search -= 1
            if search < min_v:
                search = max_v
    for cup in reversed(removed):
        cup.prev = dest
        cup.next = dest.next
        dest.next.prev = cup
        dest.next = cup
    cur = cur.next
    return cur


print(run())
