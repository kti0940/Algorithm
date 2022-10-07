dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
a = input()
ret = 0
for i in range(len(a)): # a 인풋 문자열만큼 반복
    for j in dial: # 리스트 문자열만큼 반복
        if a[i] in j: # 인풋 문자열의[i]번이 리스트 문자열에 있다면
            ret += dial.index(j)+3 # dial 리스트 내 index값을 반환하여 +3초를 더함
print(ret) # 결과값 출력