n = list(map(int, input()))

answer = 0
for i in n:
    if i <= 1 or answer <= 1:
        answer += i
    else:
        answer *= i
print(answer)