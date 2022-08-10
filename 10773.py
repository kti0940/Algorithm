import sys
k = int(sys.stdin.readline())

m = []
for i in range(k):
    money = int(sys.stdin.readline())
    if money == 0:
        m.pop()
    else:
        m.append(money)
print(sum(m))