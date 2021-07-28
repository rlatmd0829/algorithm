n, m = map(int, input().split())

demo = [int(input()) for _ in range(n)]
demo.sort()
l = 1
r = max(demo)
check = 0
while l <= r:
    mid = (l + r) // 2 # 길이

    lines = 0
    for i in demo:
        lines += i // mid # 분할된 랜선 수

    if lines >= m: # 이미 충족이 됬다면 길이를 더 늘려봐서 최대값을 찾는다.
        check = mid
        l = mid + 1
    else:
        r = mid - 1
print(check)