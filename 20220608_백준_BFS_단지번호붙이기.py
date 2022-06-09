N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))




from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, x ,y):
    # 큐 생성
    queue = deque()
    # 넣기
    queue.append((x,y))
    # 방문 처리
    graph[x][y] = 0
    # 단지 내 집 수
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                # 다시 넣기
                queue.append((nx, ny))

                # 방문 처리
                graph[nx][ny] = 0

                # count추가
                count += 1
    return count
            
# 시작점을 모르니까 1인 곳을 찾아서 우다다다 방문하자.
# graph가 업데이트 되면 
cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

print(len(cnt))
for i in range(len(cnt)):
    print(sorted(cnt)[i])