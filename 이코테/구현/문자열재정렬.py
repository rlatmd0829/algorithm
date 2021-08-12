n = list(input())
answer = []
result = 0
for i in n:
    if i.isalpha():
        answer.append(i)
    else:
        result += int(i)
answer.sort()
answer.append(str(result))
print(''.join(answer))