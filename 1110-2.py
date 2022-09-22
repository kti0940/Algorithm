n = int(input())
num = n
count = 0

while True:
    # 26의 나머지
    a = num // 10
    # 26의 몫
    b = num % 10
    # a + b 더한 수의 몫
    c = (a + b) % 10
    num = (b * 10) + c
    count +=1
    if num == n:
        break
print(count)