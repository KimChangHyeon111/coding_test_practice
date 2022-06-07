# 1260번. DFS와 BFS

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# graph 연결!
for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬. 작은 것부터 방문해야 하므로.
for i in range(len(graph)):
    graph[i].sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    # 현재 노드와 연결된 다른 노드를 재귀함수를 통해 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited)

from collections import deque
def bfs(graph, v, visited):
    # 1-1. 큐 생성하고, 시작 노드 큐에 삽입
    queue = deque([v])

    # 1-2. 그 노드 방문 처리
    visited[v] = True

    # 반복
    while queue:
        v = queue.popleft() # 2-1.다시 노드 꺼내고
        print(v, end = ' ')

        for i in graph[v]: # 2-2. 인접한 모든 노드 중에
            if not visited[i]: # 2-3. 방문하지 않은 모든 노드를
                queue.append(i) # 2-4. 큐에 넣고
                visited[i] = True # 2-5. 방문처리!

print()
visited = [False]*(N+1)
bfs(graph, V, visited)