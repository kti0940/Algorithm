word = input().lower()
word_list = list(set(word))
cnt = [] # 많이 사용된 알파뱃이 들어갈 자리

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())