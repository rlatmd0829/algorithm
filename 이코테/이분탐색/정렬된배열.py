from bisect import bisect_left, bisect_right, bisect

n, x = map(int,input().split())

value = list(map(int, input().split()))

left = bisect_left(value, x)
right = bisect_right(value, x)
print(left)
print(right)
print(bisect(value, x))
# if left - right == 0:
#     print(-1)
# else:
#     print(right - left)
