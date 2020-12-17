'''
'''


def run():
    rules = []
    names = []
    my = []
    nearby = []
    with open('./input.txt') as f:
        stage = 0
        for l in f.readlines():
            l = l.strip()
            if stage == 0:
                if l == '':
                    stage = 1
                    continue

                name, l = l.split(': ')
                names.append(name)
                raw = l.split(' or ')
                rule = []
                for seg in raw:
                    rule.append([int(n) for n in seg.split('-')])
                rules.append(rule)
            elif stage == 2:
                for item in l.split(','):
                    my.append(int(item))
                stage += 1
            elif stage < 5:
                stage += 1
            elif stage == 5:
                ticket = l.split(',')
                valid = True
                for item in ticket:
                    item = int(item)
                    item_valid = False
                    for rule in rules:
                        for seg in rule:
                            if seg[0] <= item <= seg[1]:
                                item_valid = True
                                break
                    if not item_valid:
                        valid = False
                        break
                if valid:
                    nearby.append([int(n) for n in ticket])

    assert len(rules) == len(my)
    possible = [set(range(len(rules))) for i in range(len(rules))]
    for ticket in nearby:
        for i in range(len(ticket)):
            orig = set(possible[i])
            for j in orig:
                rule = rules[j]
                valid = False
                for seg in rule:
                    if seg[0] <= ticket[i] <= seg[1]:
                        valid = True
                        break
                if not valid:
                    possible[i].remove(j)

    done = set()
    changed = True
    while changed:
        changed = False
        for i in range(len(possible)):
            if i in done:
                continue
            if len(possible[i]) == 1:
                item = list(possible[i])[0]
                changed = True
                done.add(i)
                for j in range(len(possible)):
                    if i != j and item in possible[j]:
                        possible[j].remove(item)

    values = []
    for i in range(len(my)):
        if names[list(possible[i])[0]].startswith('departure'):
            values.append(my[i])

    print(len(values))
    import math
    return math.prod(values)


print(run())
