top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # [0, 0, 0, 0, 0]
    while heights: # O(N^2)
        height = heights.pop() # [6, 9, 5, 7]
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height: # 레이저가 더 길경우 막혀서 끝난다.
                answer[len(heights)] = idx + 1 # 인덱스 값이 아니라 위치값을 넣어주는 거니까 idx+1
                break # heights에 pop을 한번 했기때문에 처음 for문 돌때 len(heights)=4 이기때문에 answer[4]에 idx+1을 넣어준다.
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!