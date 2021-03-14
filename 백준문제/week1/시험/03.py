import sys
T = int(input())

s = []

for i in range(T):
    s.append(int(sys.stdin.readline()))
    
for i in sorted(s):
    print(i)