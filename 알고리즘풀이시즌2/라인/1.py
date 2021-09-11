def solution(student, k):
    answer = 0
    for i in range(len(student)):
        cnt = 0
        for j in range(i, len(student)):
            
            if cnt > k:
                break
            
            if student[j] == 1:
                cnt += 1
                if cnt == k:
                    answer += 1
            elif student[j] == 0:
                if cnt == k:
                    answer += 1
                continue
                
    return answer