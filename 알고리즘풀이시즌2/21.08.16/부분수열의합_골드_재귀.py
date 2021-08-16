import sys
n = int(input())

value = list(map(int, input().split()))
result = []
def recursive(index, sum):
    if index == n:
        result.append(sum)
        return
    
    recursive(index+1, sum + value[index])
    recursive(index+1, sum)

recursive(0,0)
ans = 0 # 아무것도 선택안하는 경우가 있을수 있다.
result = list(set(result))
result.sort()

for i in result:
    if ans != i:
        print(ans)
        sys.exit()
    else:
        ans += 1
print(result[-1] +1)
