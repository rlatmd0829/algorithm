import sys
sys.setrecursionlimit(10**6)

n, s = map(int, input().split())

value = list(map(int,input().split()))
cnt = 0
def recursive(index, sum):
    global cnt
    if index == n:  
        if sum == s: # 정답을 찾은 경우는 index가 n인 경우에서 sum이 s랑 같은 경우이다.
                    # 그냥 sum이 s인 경우 종료시켜버리면 그 뒤에 인덱스 까지 합해서 s가 되는 경우를 버리기 때문에 안된다.
            cnt += 1
        return
    recursive(index+1, sum+value[index])
    recursive(index+1, sum)
recursive(0,0)
if s == 0:
    cnt -= 1
print(cnt)