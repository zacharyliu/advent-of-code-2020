'''
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''


def seats():
    with open('./input.txt') as f:
        for l in f.readlines():
            l = l.strip()

            x1 = 127
            x2 = 0
            for r in l[:6]:
                mid = (x1 + x2 + 1) // 2
                if r == 'B':
                    x2 = mid
                else:
                    x1 = mid - 1
            x = x1 if l[6] == 'B' else x2
            y1 = 7
            y2 = 0
            for c in l[-3:-1]:
                mid = (y1 + y2 + 1) // 2
                if c == 'R':
                    y2 = mid
                else:
                    y1 = mid - 1
            y = y1 if l[-1] == 'R' else y2

            yield x, y


def find():
    s = {}
    for r in range(0, 128):
        for c in range(0, 8):
            s[(r, c)] = True

    for seat in seats():
        r, c = seat
        s[(r, c)] = False

    min_r = None
    for (r, c), empty in s.items():
        if not empty and min_r is None:
            min_r = r
        if min_r is not None and r >= min_r and empty:
            return r * 8 + c


print(find())
