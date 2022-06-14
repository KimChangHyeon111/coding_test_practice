M, N = 6, 4
graph = [
[0, -1, 0, 0, 0, 0],
[-1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1]
]

# M, N = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(graph):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs(graph)
max_date = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    max_date = max(max_date, max(i))
print(max_date - 1)
