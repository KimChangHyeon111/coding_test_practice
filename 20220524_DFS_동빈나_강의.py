# Stack & Que
# Stack : 먼저 들어온 데이터가 나중에 나가는 구조. 선입 후출. 
# list로 구현 가능. append()와 pop()으로 가장 오른쪽에서 넣고 뺄 수 있음. 
# Que : 먼저 들어온 데이터가 먼저 나가는 구조. 선입 선출
# from collections import deque로 구현 가능. 
# que = deque()
# que.append(), que.popleft()로 선입 선출할 수 있음. 


# 재귀함수
# DFS에 자주 사용. 자기 스스로를 자꾸 호출하는 함수.
# '재귀함수를 호출합니다'를 자꾸 호출하는 함수를 만든다면
def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()

# 이런 재귀함수는 일종의 stack이라 메모리에 함수가 순서대로 stack되고, 마지막 함수부터 순서대로 종료되는 형태임. 
# 무한루프가 목적이 아니라면, 종료 조건을 주는 게 좋다.

def r_f2(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', 1+1, '번째 재귀함수를 호출합니다.')
    r_f2(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

r_f2(1) # 100번째부터 종료하는, stack형태의 자료구조임을 알 수 있음.

# 팩토리얼 구현
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1) # 재귀적으로 호출!


# 유클리드 호제법을 통한 최대공약수 구하기
# 유클리드 호제법 : A>B인 두 자연수 A,B에 대해 A%B를 R이라 할 때, A,B의 최대공약수는 B,R의 최대공약수와 같다. 
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

# 이러한 재귀함수는 복잡한 걸 간결하게 작성할 수 있게 해준다.
# 하지만 오히려 이해하기 어렵게 만들 수도. 점화식 본다고 이해하는 거 아니잖아?

# DFS
# 1. 탐색 시작 노드를 스택에 삽입 & 방문 처리
# 2. 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 그걸 스택에 넣고 방문처리. 없다면 최상단 노드 스택에서 제거
# 3. 2가 불가능할 때 까지 반복

# 각 노드가 연결된 정보
graph = [
    [], #첫 graph는 빈칸
    [2,3,8], # 1번 노드가 연결된 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7] # 8번 노드가 연결된 노드
] 

# 각 노드가 방문된 정보
visited = [False] * 9 

# dfs 함수 정의
def dfs(graph, v, visited):
    '''
    graph   : 노드 연결 정보
    v       : 탐색 시작 노드
    visited : 노드 방문 정보
    '''
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')

    # 현재 노드와 연결된 다른 노드를 재귀함수를 통해 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)            
