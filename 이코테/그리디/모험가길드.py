n = int(input())

mo = list(map(int, input().split()))
mo.sort()
answer = []
count = 0
while mo:
    answer.append(mo.pop())
    if len(answer) == answer[0]:
        count += 1
        answer = []
print(count)