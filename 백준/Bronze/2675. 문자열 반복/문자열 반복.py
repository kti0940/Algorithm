t = int(input()) # 테스트 갯수

for i in range(t): # 테스트 갯수만큼 반복
    num, s = input().split() # 반복할 횟수와, 문자열 입력 스플릿으로 구분
    text = '' # 빈 문자열 생성
    for j in s: # 입력받은 문자열 반복\
        text += int(num) * j # 입력받은 num * 문자열 text 변수 값 대입
    print(text) # 출력