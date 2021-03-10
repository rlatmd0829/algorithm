# T = int(input())
# stack = []
# max = 0
# for i in range(T):
#     a = int(input())
#     if max < a:
#         for j in range(max+1, a+1):
#             stack.append(j)
#             print('+')
#             if j == a:
#                 stack.pop()
#                 print('-')
#         max = a

#     else:
#         if (len(stack)+1 > a):
#             for j in range(a, len(stack)+1):
#                 stack.pop()
#                 print('-')
#         else:
#             for j in range(len(stack)+1, a):
#                 stack.pop()
#                 print('-')

################

n = int(input())

stack = []
result = []
count = 1
boolean = True

for i in range(n):
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
    
    