total = 0

with open('./input.txt') as f:
    for l in f.readlines():
        a, l = l.split('-')
        b, c, d = l.split(' ')
        a = int(a)
        b = int(b)
        c = c[:-1]
        
        count = sum(1 if x == c else 0 for x in d)
        if count >= a and count <= b:
            total += 1

print(total)