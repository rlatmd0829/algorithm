def solution(food_times, k):
    answer = 0
    for i in range(k):
        if i > 2:
            i = i%3
        if food_times[i] == 0:
            i += 1
            if i > 2:
                i= i % 3
        food_times[i] = food_times[i] - 1
        answer = i
        print(answer)
    
    
    answer = answer + 1
    if answer > 2:
        answer = answer % 3
    return answer+1