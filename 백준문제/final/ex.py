prices = [1,2,3,2,3]
answer = []

for i in range(len(prices)):
    r = 0
    for j in range(i+1, len(prices)):
        if prices[i] <= prices[j]:
            r += 1
        else:
            break
    answer.append(r)

print(answer)
