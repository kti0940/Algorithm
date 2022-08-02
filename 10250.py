# h = 호텔 층수
# w = 각층의 방수
# n = n번째 손님

t = int(input())

for i in range(t):
    h, w, n = map(int,input().split())
    num = n // h+1
    floor = n % h
    if n % h == 0:
        num = n//h
        floor = h
    print(f'{floor*100+num}')