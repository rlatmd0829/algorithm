def solution(dartResult):
    answer = []
    list_dartResult = list(dartResult)
    demo = []
    for i in range(len(list_dartResult)):
        if list_dartResult[i] == '1' and list_dartResult[i+1] == '0':
            demo.append('10')
        elif list_dartResult[i] == '0' and list_dartResult[i-1] == '1':
            continue
        else:
            demo.append(list_dartResult[i])
    for i in range(1,len(demo)):
        if demo[i] == 'S':
            answer.append(int(demo[i-1]))
        elif demo[i] == 'D':
            answer.append(int(demo[i-1]) ** 2)
        elif demo[i] == 'T':
            answer.append(int(demo[i-1]) ** 3)
        elif demo[i] == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif demo[i] == '#':
            answer[-1] = answer[-1] * -1
    return sum(answer)