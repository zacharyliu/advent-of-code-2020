'''
'''

monster_template = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def extract_edges(tile):
    edges = []
    edges.append(''.join(tile[0]))
    edges.append(''.join(l[-1] for l in tile))
    edges.append(''.join(tile[-1]))
    edges.append(''.join(l[0] for l in tile))
    return edges


def rotate(tile):
    new_tile = [[None for _ in range(len(tile))] for _ in range(len(tile[0]))]
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            new_tile[len(tile[0]) - j - 1][i] = tile[i][j]
    return new_tile


def flip(tile):
    return list(reversed(tile))


class Grid:

    def __init__(self, tiles):
        self.tiles = tiles
        ids = list(tiles.keys())
        self.tile_pos = {}
        placed_edges = {}
        while ids:
            id = ids.pop(0)
            tile = tiles[id]

            if not self.tile_pos:
                self.tile_pos[id] = (0, 0)
                self.stride = len(tile) - 2
            else:
                found = None
                other_side = None
                for _ in range(2):
                    for _ in range(4):
                        for side, edge in enumerate(extract_edges(tile)):
                            other_side = (side + 2) % 4
                            if (other_side, edge) in placed_edges:
                                found = placed_edges[(other_side, edge)]
                                break
                        if found is not None:
                            break
                        tile = rotate(tile)
                    if found is not None:
                        break
                    tile = flip(tile)
                if found is None:
                    ids.append(id)
                    continue

                if other_side == 0:
                    di, dj = 0, -1
                elif other_side == 1:
                    di, dj = 1, 0
                elif other_side == 2:
                    di, dj = 0, 1
                elif other_side == 3:
                    di, dj = -1, 0
                else:
                    raise Exception()

                self.tile_pos[id] = (self.tile_pos[found][0] + di,
                                     self.tile_pos[found][1] + dj)
                self.tiles[id] = tile

            for side, edge in enumerate(extract_edges(tile)):
                placed_edges[(side, edge)] = id

        self.min_i = min(v[0] for v in self.tile_pos.values())
        self.min_j = min(v[1] for v in self.tile_pos.values())

        self.tile_id = {pos: id for id, pos in self.tile_pos.items()}

    def get(self, x, y):
        i = self.min_i + (x // self.stride)
        j = self.min_j + (y // self.stride)
        tile = self.tiles[self.tile_id[(i, j)]]
        return tile[(y % self.stride) + 1][(x % self.stride) + 1]

    def size(self):
        max_i = max(v[0] for v in self.tile_pos.values())
        return (max_i - self.min_i + 1) * self.stride

    def format(self):
        return '\n'.join(''.join(self.get(x, y)
                                 for x in range(self.size()))
                         for y in range(self.size()))


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
                buf.append(list(l))
        tiles[id] = buf

    grid = Grid(tiles)
    size = grid.size()

    monster_pos = []
    monster = monster_template.split('\n')
    for _ in range(2):
        for _ in range(4):
            for x in range(0, size - len(monster[0]) + 1):
                for y in range(0, size - len(monster) + 1):
                    matches = True
                    for dx in range(0, len(monster[0])):
                        for dy in range(0, len(monster)):
                            if monster[dy][dx] == '#':
                                if grid.get(x + dx, y + dy) != '#':
                                    matches = False
                                    break
                        if not matches:
                            break
                    if matches:
                        monster_pos.append((x, y))
            monster = rotate(monster)
        monster = flip(monster)

    return grid.format().count('#') - (len(monster_pos) *
                                       monster_template.count('#'))


print(run())
