from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    time_end = 23 * 60 + 59
    dic = defaultdict(list)
    after = defaultdict(list)
    for i in records:
        cal = 0
        i = i.split()
        time = i[0].split(':')
        re_time = int(time[0]) * 60 + int(time[1])
        if i[2] == 'IN':
            dic[i[1]].append(re_time)
        elif i[2] == 'OUT':
            cal = re_time - dic[i[1]][0]
            dic[i[1]].pop()
            after[i[1]].append(cal)
    
    for i in dic.items():
        if i[1]:
            after[i[0]].append(time_end - i[1][0])
    
    sort_after = sorted(after.items())
    for i in sort_after:
        if sum(i[1]) > fees[0]:
            answer.append(fees[1] + math.ceil((sum(i[1]) - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer