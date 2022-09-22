# h = 호텔 층수
# w = 각층의 방수
# n = n번째 손님

t = int(input())

for i in range(t):
    # 6 12 10
    h, w, n = map(int,input().split())
    
    # 10 // 6 + 1 = 2
    # num = 2
    num = n // h+1
    
    # 10 % 6 = 4
    # floor = 4
    floor = n % h
    
    # 10 % 6 == 0
    if n % h == 0:
        
        # 10 // 6 = 1
        num = n//h
        
        # 10
        floor = h
    print(f'{floor*100+num}')