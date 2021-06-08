board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

# for i in v:
#     print(i)
print([num for row in board for num in row])

list = []
for row in board:
    for num in row:
        list.append(num)
print(list)