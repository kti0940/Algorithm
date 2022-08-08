num_list = [3, 55, 9, 5, 7, 11]

def is_maxcount(num):
    max_num = 0
    for i in num:
        if i > max_num:
            max_num = i
    return max_num

result = is_maxcount(num_list)
print(result)

result += 1

print(result)