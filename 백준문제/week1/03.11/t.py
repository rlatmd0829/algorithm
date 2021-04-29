answer = []

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

for i in range(len(arr1)):
    tmp = []
    for j in range(len(arr1[i])):
        tmp.append(arr1[i][j] + arr2[i][j])
    answer.append(tmp)
print(answer)