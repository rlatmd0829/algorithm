N, M = map(int, input().split())

card = []
answer = []
for i in range(N):
    card.append(list(map(int,input().split())))

for i in card:
    answer.append(min(i))

print(max(answer))
