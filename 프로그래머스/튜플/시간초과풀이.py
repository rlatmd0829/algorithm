from collections import Counter
def solution(s):
    answer = []
    count = []
    s=s.replace('{', '')
    s=s.replace('}', '')
    s=s.split(',')
    print(s)
    for i in s:
        count.append([s.count(i), i])

    set_s = set(s)
    len_set_s = len(set_s)
    
    count.sort(reverse = True)
    for i in range(len(count)):
        if count[i][0] == len_set_s:
            if count[i][1] not in answer:
                answer.append(int(count[i][1]))
                len_set_s -= 1
    
    return answer