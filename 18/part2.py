'''
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231
Here are the other examples from above:

1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
2 * 3 + (4 * 5) becomes 46.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
What do you get if you add up the results of evaluating the homework problems using these new rules?
'''


def data():
    lines = []
    with open('./input.txt') as f:
        for l in f.readlines():
            l = l.strip()
            lines.append(l)
    return lines


def evaluate(line, i):
    res = []
    op = []
    while i < len(line):
        c = line[i]
        if c == '(':
            new, i = evaluate(line, i + 1)
            res.append(new[0])
            while op and op[-1] == '+':
                op.pop()
                res.append(res.pop() + res.pop())
        elif c == ')':
            i += 1
            break
        elif c == '+' or c == '*':
            op.append(c)
            i += 1
        elif c == ' ':
            i += 1
        else:
            res.append(int(line[i]))
            while op and op[-1] == '+':
                op.pop()
                res.append(res.pop() + res.pop())
            i += 1
    while op:
        op.pop()
        res.append(res.pop() * res.pop())
    return res, i


def run():
    results = []
    for line in data():
        res, _ = evaluate(line, 0)
        results.append(res[0])
    return sum(results)


print(run())
