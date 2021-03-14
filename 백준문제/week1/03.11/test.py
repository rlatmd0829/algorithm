
node = {}
for i in range(7): # {1: [2, 5], 2: [1, 3, 5], 3: [2], 5: [1, 2, 6], 6: [5], 4: [7], 7: [4]}
    node[i+1] = []
for i in range(6):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
print(node)
    
    

    # if node.get(f) == None:
    #     node[f] = [t]
    #     if node.get(t) == None:
    #         node[t] = [f]
    #     else:
    #         node[t].append(f)
    # else:
    #     node[f].append(t)
    #     if node.get(t) == None:
    #         node[t] = [f]
    #     else:
    #         node[t].append(f)

def bfs(node, start):
    queue = [start]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for i in node[current_node]:
            if i not in visited and i not in queue:
                queue.append(i)

    return(visited)

v = bfs(node, 1)
print(v)
print(len(v)-1)