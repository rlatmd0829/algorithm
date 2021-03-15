import math

n = int(input())

for _ in range(n): # r은 x,y 에서 목표물 까지의 거리 즉, 반지름이라고 볼 수 있다.
    x1, x2, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2) # 두원의 거리 (원의 방정식 활용)

    if distance == 0 and r1 == r2: # 두 원이 동심원이고 반지름이 같을때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance: # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0) # 그 외에