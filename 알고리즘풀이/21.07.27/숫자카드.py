n = int(input())
answer = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
answer.sort()
result = []

for target in check:
    l = 0
    r = len(answer)-1
    while l <= r:
        mid = (l + r) // 2
        if target == answer[mid]:
            result.append(1)
            break
        if answer[mid] < target:
            l = mid + 1
        elif answer[mid] > target:
            r = mid - 1
    else:
        result.append(0)
for i in result:
    print(i, end=' ')
