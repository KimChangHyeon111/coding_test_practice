import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1 + N)

from collections import deque
def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)         


count = 0  

for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면, 즉 지혼자 하나의 연결요소라면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(graph, i, visited)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면, 즉 지혼자 하나의 연결요소라면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            dfs(graph, i, visited)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.


print(count)
