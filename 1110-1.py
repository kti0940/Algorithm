n = int(input())
num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    print(c)
    num = (b * 10) + c
    count += 1
    if num == n:
        break
print(count)





# n = int(input())

# num = n
# count = 0

# while True:
#     a = num // 10
#     print(f'얘는 a야 -> {a}')
#     b = num % 10
#     print(f'얘는 b야 -> {b}')
#     c = (a + b) % 10
#     print(f'얘는 c야 -> {c}')
#     num = (b * 10) + c
#     print(f'얘는 num야 -> {num}')
    
#     count += 1
#     if(num == n):
#         break
    
# print(count)