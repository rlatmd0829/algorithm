N,M,K = map(int, input().split())

N = list(map(int,input().split()))
N.sort(reverse=True)
print(N)
answer = 0
count=0
for i in range(M):
    if count == K:
        answer += N[1]
        count = 0
    else:
        answer += N[0]
        count+=1
    

print(answer)
    

