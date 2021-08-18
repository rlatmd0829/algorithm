import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 1:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
        else:
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            heapq.heappush(scoville, x+y*2)
            answer += 1
        
    return answer