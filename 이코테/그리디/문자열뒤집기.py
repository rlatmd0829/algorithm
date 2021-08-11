n = list(map(int, input()))
count1 = 0 # 전부 0으로 바꾸는 경우
count0 = 0 # 전부 1로 바꾸는 경우

if n[0] == 1:
    count0 += 1
else:
    count1 += 1

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == 1:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))