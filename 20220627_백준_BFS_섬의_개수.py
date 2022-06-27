# w = 5
# h = 4
# graph = [
#     [1,0,1,0,0],
#     [1,0,0,0,0],
#     [1,0,1,0,1],
#     [1,0,0,1,0]
# ]

# w = 5
# h = 5

# graph = [
#     [1,0,1,0,1],
#     [0,0,0,0,0],
#     [1,0,1,0,1],
#     [0,0,0,0,0],
#     [1,0,1,0,1]
# ]


dx = [-1,-1,-1,1,1,1,0,0]
dy = [1,0,-1,1,0,-1,1,-1]

from collections import deque

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

# result = 0
# for i in range(h):
#     for j in range(w):
#       if graph[i][j] == 1:
#         bfs(graph, i, j)
#         result += 1

# print(result)

while True:
    w, h = map(int, input().split())
    graph = []
    
    if w == h == 0:
        break

    else :    
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        result = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(graph, i, j)
                    result += 1
        print(result)
