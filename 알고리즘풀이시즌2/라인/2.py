from collections import defaultdict
from collections import Counter
def solution(research, n, k):
    answer = []
    eng = []
    result = defaultdict(list)
    for i in research:
        set_i = set(i)
        for j in set_i:
            if j not in eng:
                eng.append(j)
    for i in eng:
        for j in research:
            result[i].append(j.count(i))
    
    for i in result.items():
        for j in range(len(i[1])):
            demo = 0
            for w in range(0, len(i[1])-n+1):

                count = 0
                for m in range(w, w+n):
                    if i[1][m] >= k:
                        count += 1
                
                if count == n and sum(i[1][w:w+n]) >= 2*n*k:
                    answer.append(i[0])
                    
            counter = Counter(answer)
            
    if counter:
        ans = counter.most_common()
        ans.sort(key = lambda x : (-x[1],x[0]))
        answer = ans[0][0]
        return answer
    else:
        return "None"