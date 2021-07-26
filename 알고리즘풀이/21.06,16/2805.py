n, m = map(int,input().split())

h = list(map(int,input().split()))



def binary(arr, target):
    answer = 0
    min_arr = min(arr)
    max_arr = max(arr)
    mid_arr = (min_arr + max_arr) // 2
    for i in arr:
        if i > mid_arr:
            answer += i - mid_arr
