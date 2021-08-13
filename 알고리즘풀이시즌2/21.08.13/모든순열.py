from itertools import permutations
n = int(input())

per = list(permutations(range(1,n+1),n))
answer = []
for i in per:
    i = list(i)
    answer.append(i)
answer.sort()
for i in answer:
    for j in i:
        print(j, end=' ')
    print()
# answer = []
# for i in per:
#     i = list(i)
#     i.sort()
#     if i not in answer:
#         answer.append(i)

# for i in answer:
#     for j in i:
#         print(j, end=' ')
#     print()
