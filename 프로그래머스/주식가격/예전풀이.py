def solution(prices):
    answer = []
    for i in range(len(prices)):
        r = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                r += 1
            else:
                r += 1
                break
        answer.append(r)
    return answer