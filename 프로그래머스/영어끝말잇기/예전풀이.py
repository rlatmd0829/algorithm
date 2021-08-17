def solution(n, words):
    answer = []
    temp = []
    temp.append(words[0])
    result1 = 0
    result2 = 0
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0]:
            if words[i] not in temp:
                temp.append(words[i])
            else:
                result1 = i % n + 1 # 몇번째 사람이 떨어졌는지
                result2 = i // n + 1 # 떨어진 사람이 몇번째에 떨어졌는지
                return [result1, result2]
        else:
            result1 = i % n + 1 # 몇번째 사람이 떨어졌는지
            result2 = i // n + 1 # 떨어진 사람이 몇번째에 떨어졌는지
            return [result1, result2]
    else:
        return [0,0]