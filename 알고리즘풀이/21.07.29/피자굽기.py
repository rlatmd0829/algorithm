d, n = map(int, input().split())

oven = list(map(int, input().split()))
answer = list(map(int, input().split()))

for i in range(len(oven)-1): # 현재 오븐은 내림차순으로 되어있다.
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]

check = 0 # 도우가 어느 오븐에 쌓였는지
l = 0
r = len(oven) - 1
for i in answer:
    is_piled = False # 피자가 오븐에 들어올 수 없으면 false

    while l <= r:
        mid = (l + r) // 2
        current = oven[mid]
        if current >= i: # 만약 현재 오븐의 지름이 더 크다면 더 작은값을 찾아본다 (내림차순 이므로 l = mid + 1)
            l = mid + 1
            check = mid
            is_piled = True
        else: # 현재 오븐의 지름이 더 작다면 피자가 들어갈 수 없다.
            r = mid - 1
    
    if not is_piled: # false일경우
        check = -1
        break

    l = 0
    r = check - 1 # 도우가 쌓인 오븐 이전값에만 쌓일 수 있다.

if check == -1:
    print(0)
else:
    print(check+1) # 인덱스 값이므로 +1 해줘야함

