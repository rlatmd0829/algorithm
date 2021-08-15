from itertools import combinations
su = [int(input()) for _ in range(9)]

com = list(combinations(su, 7))
answer = []
for i in com:
    if sum(i) == 100:
        answer.extend(i)

for i in answer:
    print(i)

