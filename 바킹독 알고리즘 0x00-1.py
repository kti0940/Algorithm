n = int(input())

def isDrainage(n):
    ret = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            ret += i
    print(ret)
    return ret
isDrainage(n)