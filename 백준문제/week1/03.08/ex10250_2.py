T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    
    if N%H == 0: # 딱 떨어지는 경우
        h = H
        w = N//H
    else:
        h = N%H #층
        w =N//H+1 #호수

    print(cmd*100+ho)

