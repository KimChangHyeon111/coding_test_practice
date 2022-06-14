# 2606번.바이러스

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

# 1012번.유기농배추
# import sys
# sys.setrecursionlimit(10000)
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# for i in range(4):
#     print(dx[i])

# def dfs2(graph, x, y):
#     if x < 0 or y < 0 or x >= m or y >= n:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs2(graph, nx, ny)
#             return True
#     return False

# t = int(input())

# for i in range(t):
#   # 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수
#   m,n,k = map(int, input().split())
#   graph = [[0]*m for _ in range(n)]
#   result = 0
  
#   # 배추 위치에 1 표시
#   for i in range(k):
#     a,b = map(int,input().split())
#     graph[b][a] = 1

#   # DFS를 활용해서 배추 그룹 수 세기
#   for i in range(m):
#     for j in range(n):
#       if graph[j][i] == 1:
#         dfs2(i, j)
#         result += 1
  
#   # 출력
#   print(result)   


# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

# DFS 정의 
def dfs(x,y):
  # 상,하, 좌,우
  dx = [1, -1, 0, 0] 
  dy = [0, 0, 1, -1]
   
  for i in range(4): 
    nx = x + dx[i] 
    ny = y + dy[i]
    if (0 <= nx < m) and (0 <= ny < n): 
      if graph[ny][nx] == 1:
      	# 방문했다는 표시 -1
        graph[ny][nx] = -1
        dfs(nx, ny)

# 테스트 케이스      
t = int(input())

for i in range(t):
  # 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수
  m,n,k = map(int, input().split())
  graph = [[0]*m for _ in range(n)]
  result = 0
  
  # 배추 위치에 1 표시
  for i in range(k):
    a,b = map(int,input().split())
    graph[b][a] = 1

  # DFS를 활용해서 배추 그룹 수 세기
  for i in range(m):
    for j in range(n):
      if graph[j][i] == 1:
        dfs(i, j)
        result += 1
  
  # 출력
  print(result)   

