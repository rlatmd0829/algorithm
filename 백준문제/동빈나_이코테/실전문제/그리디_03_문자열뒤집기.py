array = input()

count0 = 0 # 전부 0으로 만드는 횟수
count1 = 0 # 전부 1로 만드는 횟수

if array[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(array)-1):
    if array[i] != array[i+1]:
        if array[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))

    