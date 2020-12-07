'''
'''


def data():
    total = 0
    qs = set()
    first = True
    with open('./input.txt') as f:
        for l in f.readlines():
            l = l.strip()

            if l == '':
                total += len(qs)
                qs = set()
                first = True
            else:
                qs2 = set()
                for c in l:
                    qs2.add(c)
                if first:
                    qs = qs2
                    first = False
                else:
                    qs = qs & qs2

    total += len(qs)
    return total


print(data())
