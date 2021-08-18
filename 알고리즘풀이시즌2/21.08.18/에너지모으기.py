n = int(input())

en = list(map(int, input().split()))
maxx = 0
def recursive(en,sum):
    global maxx
    if len(en) == 2:
        maxx = max(maxx, sum)
        return
    
    for i in range(1,len(en)-1):
        sum += (en[i-1] * en[i+1])
        b = en[:i] + en[i+1:]
        recursive(b,sum)
        sum -= (en[i-1] * en[i+1]) # 이게 dfs와 다른점 아마..
        # 재귀를 통해 쭉 들어갔다가 다시 올라오니까 다음 for 문을 돌떄는 sum에 값이 남아잇으면 안된다.

recursive(en,0)
print(maxx)
