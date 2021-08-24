n = int(input())

value = list(map(int, input().split()))

l = 0
r = len(value) - 1
check = 0
while l <= r:
    mid = (l+r) // 2

    if mid == value[mid]:
        check = mid
        break
    if value[mid] > mid:
        r = mid - 1
    else:
        l = mid + 1
if check == 0:
    print(-1)
else:
    print(check)