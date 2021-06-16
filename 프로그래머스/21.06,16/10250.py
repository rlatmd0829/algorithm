T = int(input())


for i in range(T):
    h,w,n = map(int,input().split())
    cmd = n % h
    if cmd == 0:
        cmd = h
        ho = n // h
    else:
        ho = n // h + 1
    print(cmd * 100 + ho)
