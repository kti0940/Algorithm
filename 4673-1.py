# natural_num = set(range(1, 10001)) # 자연수를 1~10000까지 변수설정
# generated_num = set() #생성될 숫자를 넣어줄 변수

# for i in range(1,10001): #1부터 10000까지 반복문
#     for j in str(i): #입력되는 i를 str로 바꿔주면서 반복문 ex) 850 = "8","5","0"
#         i += int(j) # 850 + 8 + 5 + 0, i = 863
#     generated_num.add(i) # 생성자가 있는 숫자들을 넣어줌
    
# self_num = sorted(natural_num - generated_num) #전체 자연수에서 생성자가 모인 변수를 빼줌
# for i in self_num: #for 문을 돌려서 print로 생성자가 없는 셀프넘버를 출력함
#     print(i)

num = set(range(1, 10001))
num2 = set()

for i in range(1, 21):
    for j in str(i):
        # print(j)
        i += int(j)
    num2.add(i)

self_num = sorted(num - num2)
for i in self_num:
    print(i)