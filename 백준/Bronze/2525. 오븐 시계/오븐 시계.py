H, M = map(int, input().split())
cooktime = int(input())

H += cooktime // 60
M += cooktime % 60

if M >= 60:
    H += 1
    M -= 60
    
if H >= 24:
    H -= 24
    
print(H, M)