T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    
    if N%H == 0: # 딱 떨어지는 경우
        cmd = H
        ho = N//H
    else:
        cmd = N%H #층
        ho =N//H+1 #호수

    print(cmd*100+ho)

