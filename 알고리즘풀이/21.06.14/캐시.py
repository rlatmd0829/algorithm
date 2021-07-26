def solution(cacheSize, cities):
    answer = 0
    stack = []
    for i in cities:
        if cacheSize == 0:
            return 5 * len(cities)
        i = i.lower()
        if i in stack:
            stack.remove(i)
            stack.append(i)
            answer += 1
        else:
            answer += 5
            stack.append(i)
            if len(stack) > cacheSize:
                stack.pop(0)
    return answer

    