n = int(input())

for i in range(n):
    s = input()
    a = 0
    b = 0
    for j in s:
        if j=='O':
            b += 1
        else:
            b = 0
        a += b
    print(a)