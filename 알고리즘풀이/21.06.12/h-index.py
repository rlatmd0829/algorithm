def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1, len(citations)+1):
        num = citations[-i]
        if num >= i:
            answer = i
    return answer