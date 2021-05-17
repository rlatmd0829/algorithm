n = int(input())

list = [int(input()) for _ in range(n)]

# list = []
# for i in range(n):
#     list.append(int(input()))


list.sort(reverse=True)
print(list)