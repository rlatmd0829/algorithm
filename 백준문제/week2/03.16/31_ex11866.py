N, K = map(int,(input().split()))

josephus = [i for i in range(1,N+1)]
result = []
l = len(josephus)
plus = K                        # 더해주는 값은 고정이므로 변하지 않게 따로 저장해둠

while josephus:                 # 1,2,3,4,5,6,7 일때 K=7일때 7을 빼야하므로 나머지 연산해서 0인경우는 7에 값을 계속 가지고 있게 만들어준다.
    if K % len(josephus) == 0:  # K 값은 인덱스 값이 아니므로 0이 되면 안된다. ex) 5, 6, 7 이 있을때 3인 값을 뽑고 싶다고 하면 index로 2인 7인 값을 뽑아줘야 하는데 나머지 연산으로 0이 되기 때문에 나머지 연산이 0인경우는 그대로 K의 값을 유지할 수 있게해준다.
        K = len(josephus)
    else:
        K = K % len(josephus)   # K를 한번 돌때마다 plus값을 더해 줄거기 때문에 길이를 벗어나면 다시 0부터 시작할 수 있도록 나머지 연산을 해준다.
    K = K-1                     # K=3일때 인덱스값으로는 2인 인덱스를 빼야하기 때문에 -1을 해준다.
    result.append(josephus.pop(K))
    K = K + plus                # K값에서 계속 진행하기위해서 K값에 plus 값을 더해준다.

print('<'+', '.join(map(str,result))+'>')