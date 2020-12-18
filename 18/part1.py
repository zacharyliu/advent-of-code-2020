'''
As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71
Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51
Here are a few more examples:

2 * 3 + (4 * 5) becomes 26.
5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?
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
    op = None
    while i < len(line):
        c = line[i]
        if c == '(':
            new, i = evaluate(line, i + 1)
            res.append(new[0])
            if op is not None:
                assert len(res) == 2
                res = [op(res[0], res[1])]
                op = None
        elif c == ')':
            return res, i + 1
        elif c == '+':
            op = lambda a, b: a + b
            i += 1
        elif c == '*':
            op = lambda a, b: a * b
            i += 1
        elif c == ' ':
            i += 1
        else:
            res.append(int(line[i]))
            if op is not None:
                assert len(res) == 2
                res = [op(res[0], res[1])]
                op = None
            i += 1
    return res, i


def run():
    results = []
    for line in data():
        res, _ = evaluate(line, 0)
        results.append(res[0])
    return sum(results)


print(run())
