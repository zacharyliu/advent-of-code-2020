total = 0

with open('./input.txt') as f:
    for l in f.readlines():
        a, l = l.split('-')
        b, c, d = l.split(' ')
        a = int(a)
        b = int(b)
        c = c[:-1]
        
        if d[a-1] == c and d[b-1] != c or d[a-1] != c and d[b-1] == c:
            total += 1

print(total)
