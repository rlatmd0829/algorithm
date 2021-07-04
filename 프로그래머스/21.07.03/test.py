from collections import defaultdict
import sys
graph = {}
print(graph)

for i in range(5):
    graph[i+1] = []
print(graph)
for _ in range(5):
    y, x = map(int, sys.stdin.readline().split())
    graph[y].append(x)
    graph[x].append(y)

print(graph)