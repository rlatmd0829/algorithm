T = int(input())

stack = []
result = []
count = 1
boolean = True
for i in range(T):
    a = int(input())
    while count <= a:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == a:
        stack.pop()
        result.append('-')
    else:
        boolean = False
        break

if boolean == False:
    print('NO')
else:
    for i in result:
        print(i)