T = int(input())
stack = []
result = 0
for i in range(T):
    a = int(input())
    if a == 0:  # 입력값에 0이 들어오면 스택에서 하나 뺴준다
        stack.pop()
    else: # 입력값을 스택에 넣어준다
        stack.append(a)

for i in stack: # 스택에 모든값 더해줌
    result += i
print(result)