cnt0 = [1, 0]
cnt1 = [0, 1]

for i in range(2, 41): # 입력 값 3에 대한 0 호출회수 = (입력 값 2에 대한 0 호출회수) + (입력 값 1에 대한 0 호출회수)
                       # 입력 값 3에 대한 1 호출회수 = (입력 값 2에 대한 1 호출회수) + (입력 값 1에 대한 1 호출회수)
    cnt0.append(cnt0[i-1]+cnt0[i-2])
    cnt1.append(cnt1[i-1]+cnt1[i-2])
    
for _ in range(int(input())):
    n = int(input())
    print(cnt0[n], cnt1[n])