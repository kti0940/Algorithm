n = int(input())
nums = list(map(int, input().split()))
max_score = max(nums)

new_list = [score/max_score*100 for score in nums]
avg = sum(new_list)/n
print(avg)