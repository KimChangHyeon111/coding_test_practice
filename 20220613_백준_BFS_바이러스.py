
N_pc = 7
N_pair = 6
graph = [
    [],
    [2,5],
    [1,3,5],
    [2],
    [7],
    [1,2,6],
    [5],
    [4]
]


N_pc = int(input())
N_pair = int(input())
graph = [[] for _ in range(N_pc+1)]
for _ in range(N_pair):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N_pc+1)

# DFS풀이
count = 0
def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    return count

print(dfs(graph, 1, visited))


# BFS풀이
from collections import deque
def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    count = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True
    return count

print(bfs(graph, 1, visited))
