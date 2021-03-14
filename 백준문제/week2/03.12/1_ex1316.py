T = int(input())
result = 0
for i in range(T):
    a = input()
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            if a[j] in a[j+1:]:
                break
    else:
        result += 1
print(result)

            

