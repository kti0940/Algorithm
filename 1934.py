# import math

# n = int(input())

# for i in range(n):
#     a, b = map(int, input().split())
    
#     print(math.lcm(a, b))
    

num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a, b = b, a
    gcd = b
    lcm = A * B //b
    print(lcm)