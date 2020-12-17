'''
'''


def run():
    rules = []
    invalid = []
    with open('./input.txt') as f:
        stage = 0
        for l in f.readlines():
            l = l.strip()
            if stage == 0:
                if l == '':
                    stage = 1
                    continue

                _, l = l.split(': ')
                raw = l.split(' or ')
                for rule in raw:
                    rules.append([int(n) for n in rule.split('-')])
            elif stage < 5:
                stage += 1
            elif stage == 5:
                for item in l.split(','):
                    item = int(item)
                    valid = False
                    for rule in rules:
                        if rule[0] <= item <= rule[1]:
                            valid = True
                            break
                    if not valid:
                        invalid.append(item)

    return sum(invalid)


print(run())
