from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    stop = []
    de = defaultdict(list)
    dic = defaultdict(list)
    for i in report:
        i = i.split()
        if i[0] not in dic[i[1]]:
            dic[i[1]].append(i[0])
    
    for i in dic.items():
        if len(i[1]) >= k:
            stop.append(i[0])
    
    
    for i in stop:
        for j in dic.items():
            if i == j[0]:
                for k in j[1]:
                    de[k].append(1)
    for i in id_list:
        answer.append(len(de[i]))
    return answer