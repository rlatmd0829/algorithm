def solution(files):
    answer = []
    for i in files:
        HEAD, NUMBER, TAIL = '','',''
        number_check = False
        for j in range(len(i)):
            if i[j].isdigit():
                NUMBER += i[j]
                number_check = True
            elif not number_check:
                HEAD += i[j]
            else:
                TAIL += i[j:]
                break
        answer.append((HEAD, NUMBER, TAIL))
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬
    return [''.join(t) for t in answer]