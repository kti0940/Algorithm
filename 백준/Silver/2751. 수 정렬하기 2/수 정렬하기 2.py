import sys

n = int(input())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

nums = sorted(num)

for i in nums:
    print(i)