'''
'''


def data():
    total = 0
    qs = set()
    with open('./input.txt') as f:
        for l in f.readlines():
            l = l.strip()

            if l == '':
                total += len(qs)
                qs = set()
            else:
                for c in l:
                    qs.add(c)

    total += len(qs)
    return total


print(data())
