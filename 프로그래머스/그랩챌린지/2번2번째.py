def solution(grades):
    answer = []
    answer2 = []
    result_grades = []
    result = []
    value = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D+', 'D0', 'D-', 'F']
    cnt = 0
    for grade in grades:
        grade += ' '+str(cnt)
        result_grades.append(list(grade.split()))
        cnt+=1
        
    cnt = 0
    for i in range(len(result_grades)):
        if answer:
            for j in range(len(answer)):
                if result_grades[i][0] == answer[j][0]:
                    if value.index(answer[j][1]) <= value.index(result_grades[i][1]):
                        break
                    else:
                        answer.pop(j)
                        answer.append(result_grades[i])
                        #answer[j][1] = result_grades[i][1]
                        break
            else:
                answer.append(result_grades[i])
        else:
            answer.append(result_grades[i])
            
    demo = []
    for i in answer:
        if value.index(i[1]) not in demo:
            demo.append(value.index(i[1]))
    demo.sort()
    
    
    answer.sort(key = lambda x : (x[1],x[2]))
    
    # for i in demo:
    #     for j in answer:
    #         if i == value.index(j[1]):
    #             answer2.append(j)
    
    for i in answer:
        result.append(' '.join(i[0:-1]))
    return result