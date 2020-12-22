'''
'''

import math
from collections import defaultdict


def normalize(edge):
    edge = ''.join(edge)
    rev = ''.join(reversed(edge))
    return rev if rev < edge else edge


def run():
    tiles = {}
    with open('./input.txt') as f:
        id = None
        buf = []
        for l in f.readlines():
            l = l.strip()
            if id is None:
                id = int(l[5:-1])
            elif l == "":
                tiles[id] = buf
                id = None
                buf = []
            else:
                buf.append(l)
        tiles[id] = buf

    edge_map = defaultdict(list)
    for id, tile in tiles.items():
        edges = []
        edges.append(normalize(tile[0]))
        edges.append(normalize(tile[-1]))
        edges.append(normalize(l[0] for l in tile))
        edges.append(normalize(l[-1] for l in tile))
        for edge in edges:
            edge_map[edge].append(id)

    unique = defaultdict(int)
    for ids in edge_map.values():
        if len(ids) == 1:
            unique[ids[0]] += 1

    corners = []
    for id, count in unique.items():
        if count == 2:
            corners.append(id)

    assert len(corners) == 4
    return math.prod(corners)


print(run())
