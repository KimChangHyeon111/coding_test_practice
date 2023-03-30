# coding_test_practice

### Day1.
##### 20220425_로또의_최고_순위와_최저_순위_Lv1.py
배운 것
1. 특정 값이 리스트에 있는 개수를 알고 싶다면, in으로 복잡하게 loop을 돌릴 필요 없이 list.count(value)로 가능하다.
2. rank는 괜히 if절을 써서 코드를 복잡하게 만들지 말고 list와 index를 이용하거나, dictionary를 통해 오류를 막는 것이 좋다.
3. List Comprehension
```python
true_value if 조건 else false_value
```
------------


### Day2.
##### 20220426_신규_아이디_추천_Lv1.py
배운 것
1. 정규 표현식에 대한 개념 다시 정리
- []  : []사이의 문자들 중 하나와 매치. []사이의 문자들은 ^를 제외한 어떤 것도 사용 가능함. 
- \-   : 두 문자 사이의 범위 전체와 매치.
- ^   : []안에서는 조건의 부정, 밖에서는 문자열의 시작을 뜻함.
- \d  : 숫자와 매치
- \D  : 숫자가 아닌 것과 매치
- \w  : = [0-9a-zA-z]. 숫자와 알파벳에 매치
- \W  : = [^0-9a-zA-z]. 숫자와 알파벳 아닌 것과 매치
- .   : \n 제외 모든 것과 매치
- \*  : * 바로 앞의 문자가 0회 이상 반복되는 것과 매치

    Q. ca\*t라면? A.ct, cat, caaat모두 매치
- \+   : + 바로 앞의 문자가 1회 이상 반복되는 것과 매치

    Q. ca+t라면? A.cat, caaat와 매치, ct는 X
- {}  : 반복횟수 지정.
  - {n} : 정확히 n회 반복
  - {m, n} : m이상 n이하 반복

- ?   : = {0,1}. ?앞의 문자가 있거나 없는 것과 매치

    Q. ca?t라면? A.ct, cat와 매치, caaat는 X
    
- Raw string : 문자열 앞에 r을 붙여서 \\ = \이되기 때문에 \\\\를 입력하는 불상사를 예방하는 것. 


2. Re.sub(pattern, repl, string)
------------

### Day3.
##### 20220427_숫자_문자열과_영단어_Lv1.py
배운 것
- re.sub은 엄밀히 따지면 정규표현식을 위한 함수고, string은 string.replace(old, new)로도 대체가 가능하다. 
- 이 때 old, new를 각각 key, value로 가지는 dict를 만들어두면
```
for key, value in dict.items():
    string = string.replace(key, value)
```
형태로 깔끔하게 정리가 가능하다.

--------------
### Day5.
##### 20220429_스킬체크_Lv1.py
배운 것
- int형의 객체는 len이 먹지 않음. len(str(6))을 써야 정상적으로 길이를 확인할 수 있음.
- 오늘까지 Lv1 마무리 하고 다음주 부터는 Lv2를 풀어보자.
- 라고 하려 했으나 하나더

##### 20220429_기능개발_Lv2.py
배운 것
- 소요 '일자'는 무조건 Ceil이다.
- math.ceil, np.ceil등이 가능하지만, 둘 다 막혔다면 //1을 이용하자. //1은 기본적으로 내림의 기능을 가지고 있으므로. 반대로 -(-float//1)는 올림과 같다. (오늘의 감탄 포인트)
- 이 과제 역시 비교 대상이 되는 잔여 일자와 최종적으로 한번에 배포되는 기능 2가지의 값을 지속적으로 가져야 하기 때문에 zip을 떠올렸어야 한다
- np.array는 element wise operation을 지원하지만 list는 아니다. list의 경우 +는 그냥 append, \*는 rep의 기능을 갖는다.
```
a = [1,2,3,4]
b = np.array(a)
a*4
> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

b*4
> array([ 4,  8, 12, 16])
```
--------------
### Day6.
##### 20220501_더_맵게_Lv2.py
배운 것
- 최소힙은 별도의 자료 구조는 아니고 heapq 모듈을 통해 원소를 추가 / 삭제한 리스트를 말함.
- 최소힙은 언제나 원소들이 정렬된 상태로 추가 / 삭제되며, 가장 작은 값이 인덱스 0에 위치함.
- 최소힙은 자체적으로 정렬이 되는 기능이 있기 때문에 list.remove(min(list))에 대비해 연산의 시간 복잡도 측면에서 이득을 가짐 (o(log(N)))
- 최소힙은 이진트리 기반이기 때문에, 부모 - 자식간의 대소 구분은 확실하지만, 자식간의 대소는 그렇지 않음. 즉, head[0]은 최소이나, heap[1]은 두 번째로 작은 숫자가 아닐 수 있음. 따라서 두 번째 작은 원소를 얻으려면 heappop으로 가장 작은 원소를 제거하고, 다시 heap[0]으로 접근해야 함.
- 힙은 리스트와 비슷하게 함수를 적용하면 원래의 힙이 update되는 식임. pop을 적용하면 return은 pop된 원소고, 원래의 list에서는 그 값이 빠지는 것도 동일.
- 힙에 튜플이 원소로 추가 / 삭제되면 튜플 내의 맨 앞의 값을 기준으로 최소 힙을 생성

```python
# 리스트 힙으로 변환
import heapq
heap = [4,1,7,3,8,5]
heapq.heapify(heap)
> [1, 3, 5, 4, 8, 7]

# 힙에 원소 추가
heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)
> [1, 3, 7, 4] 
# 보다시피 index 3에 위치한 4는 index 1에 위치한 3보다는 작기 때문에 Tree level에서는 문제가 되지 않음. 다만 전체가 정렬이 되어있는 것이 아니라는 것을 다시 확인 가능.

# 힙에서 가장 작은 원소 제거
print(heapq.heappop(heap))
print(heap)
1
[3, 4, 7]

# 최대 힙
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```
--------------
### Day7.
##### 20220503_가장_큰_수_Lv2.py
배운 것
- `dict(zip(a,b))`하면 set 취급을 받아 중복 원소가 제거됨
- `itertools.permutations`는 O(N^2)의 시간복잡도를 가져 코테용으로는 매우 부적합
- list.sort에서 key = lambda 적용 가능. 굳이 index를 찾고, argsort를 하고 할 필요가 없음. 
```
>>> numbers = [11,22,33,44,5]
>>> numbers = list(map(str, numbers))
>>> numbers.sort(key = lambda x : x*3, reverse = True)
>>> numbers
['5', '44', '33', '22', '11']
```
- 위의 사례처럼 문자열 비교는 [0]번째 값의 ASCII코드부터 비교됨. 
- input 변수의 길이나 생김새를 꼭 잘 보자. 좀 더 멋지게 풀 수 있을지도. 
- functools.cmp_to_key를 통해 특수한 정렬을 사용하자
```
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
# 2개의 값을 붙여서 크기를 비교하는 문제였으니, 일반적인 비교 연산으로는 불가능해서 이처럼 별개의 비교연산함수를 생성해준다.
# -1은 앞서서 들어온, 즉 a가 먼저 나온다는 것이고, 1은 나중에 들어온, 즉 b가 먼저 나온다는 것이다.
```
----------------------------------------------------------------------
### Day8.
##### 20220504_124_나라의_숫자_Lv2.py
배운 것
- divmod함수를 통해 몫과 나머지를 한번에 객체로 반환할 수 있다. 
```
몫, 나머지 = divmod(나누어질 수, 나눌 수)
```
- 재귀함수와 재귀문의 시간 복잡도에 대해서는...다시 공부해봐야겠다. 못 찾겠다.
- string.replace보다 indexing이 미세하게나마 빠른 것으로 보인다. 좀 더 보자.
- 근데 인간적으로 효율성 테스트는 기준을 알려주고 내가 얼마나 걸렸는지를 알려줘야 하는 거 아니냐 짜증나넨
----------------------------------------------------------------------
### Day9.
##### 20220509_오픈채팅방_Lv2.py
배운 것
```
dict.update({key:new_value})
# 이렇게 key에 해당하는 value를 업데이트 해줄 수 있고, key가 없는 값이라면 새로 넣을 수도 있음

str.startswith('string')
str.endswith('string')
#이런 식으로 문자열에 대한 조건을 사용할 수 있음
```
- dict에 대해 동일 key에 대해 복수의 value가 들어가면 나중에 들어온 값으로 업데이트 되는 듯.

```
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
id={info.split()[1]:info.split()[2] for info in record if info.split()[0]!="Leave"}
id
>>> {'uid1234': 'Prodo', 'uid4567': 'Ryan'}

```
----------------------------------------------------------------------
### Day10.
##### 20220510_뉴스_클러스터링_Lv2.py
배운 것

- 자꾸 리스트 인덱싱 하려고 하지 말고 list comprehension에 if 조건을 써서 만드는 연습을 하자
```
[str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])] #이런 식으로
```
- ```set(str1) & set(str2)```, ```set(str1) | set(str2)```이런 식으로 교 / 합집합을 구할 수 있다. 다만 set이니까 중복 제거되는 건 감안해야 한다.
- ```isalpha, isdigit, isalnum``` 함수로 굳이 정규표현식 없이도 간단하게 사용할 수 있다.
- ```append```와는 다르게 ```extend```는 리스트를 통째로 집어넣지 않는다. 통으로 넣고 싶은 게 아니라면 extend를 쓰자.


----------------------------------------------------------------------
### Day11.
##### 20220523_GREEDY_동빈나_강의.py
배운 것
https://www.youtube.com/watch?v=2zjoKjt97vQ

#### Greedy 알고리즘
- 그 순간에 가장 최적의 선택만 하면 답이 되는 것. 
- 예를 들어 1260원을 거슬러 준다면, 먼저 500원짜리부터 줄 수 있는 가장 많은 수를 주고, 그 다음에 100원짜리를 주고 하는 식으로 최적의 해를 찾는 것.
- 이런 알고리즘을 쓰기 위해선 정당성을 분석해야 함. 위의 경우 큰 단위가 작은 단위의 배수고, 작은 단위의 조합으로 다른 해를 만들어낼 수 없게 되므로 정당!
- 그 다음에 루프를 태워서 각 순간마다 Best를 찾아내면 됨.
- ```n - (n//k)*k```를 하면, 나누어 떨어지기까지 필요한 -1의 개수를 한 번에 찾을 수 있음. 
- ```result += (n-1) ```를 하면, 1이 될 때 까지 필요한 -1의 개수를 한 번에 알 수 있음. 
- K이상을 가진 사람을 어쩌구 하면 정렬을 해서 최소값부터 찾아보는 Greedy를 의심해보자.

----------------------------------------------------------------------
### Day12.
##### 20220524_DFS_동빈나_강의.py
배운 것
https://www.youtube.com/watch?v=7C9RgOcvkvo

#### Stack & Que
- Stack : 먼저 들어온 데이터가 나중에 나가는 구조. 선입 후출. 
- list로 구현 가능. append()와 pop()으로 가장 오른쪽에서 넣고 뺄 수 있음. 
- Que : 먼저 들어온 데이터가 먼저 나가는 구조. 선입 선출
```
from collections import deque
que = deque()
que.append(), que.popleft() #로 구현 가능. 
```

#### 재귀함수
- DFS에 자주 사용. 자기 스스로를 자꾸 호출하는 함수.
- '재귀함수를 호출합니다'를 자꾸 호출하는 함수를 만든다면
```
def recursive_function():
    print('재귀함수를 호출합니다')
    recursive_function()
```
- 이런 재귀함수는 일종의 stack이라 메모리에 함수가 순서대로 stack되고, 마지막 함수부터 순서대로 종료되는 형태임. 
- 무한루프가 목적이 아니라면, 종료 조건을 주는 게 좋다.
```
# stack과 종료조건
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
```

#### DFS
1. 탐색 시작 노드를 스택에 삽입 & 방문 처리
2. 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 그걸 스택에 넣고 방문처리. 없다면 최상단 노드 스택에서 제거
3. 2가 불가능할 때 까지 반복

```
# 구현

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

```

----------------------------------------------------------------------
### Day13.
##### 20220525_BFS_동빈나_강의.py
배운 것
https://www.youtube.com/watch?v=7C9RgOcvkvo

#### BFS
- 가까운 노드부터 먼저 탐색하는 알고리즘
- 큐 자료구조 활용함
- 최단 경로! 그래프의 depth! 탐색 문제에 많이 사용함. 

1. 시작 노드를 큐에 넣고 방문 처리
2. 큐에서 그 노드를 다시 꺼낸 뒤에 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두! 큐에 넣고 방문 처리
3. 2.를 못할 때 까지 반복
```
# 구현
# BFS는 queue 자료구조를 사용하기 때문에 deque를 import!
from collections import deque

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
def bfs(graph, v, visited):
    '''
    graph   : 노드 연결 정보
    v       : 탐색 시작 노드
    visited : 노드 방문 정보
    '''
    # 1-1. 큐 생성하고, 시작 노드 큐에 삽입
    queue = deque([v])
    
    # 1-2. 그 노드 방문 처리
    visited[v] = True

    # 반복
    while queue: # 3. 2.가 더는 불가능 할 때까지!
        v = queue.popleft() # 2-1. queue에서 넣었던 노드를 꺼내고
        print(v, end = ' ')
        
        for i in graph[v]: # 2-2. 인접한 모든 노드에 대해
            if not visited[i] : #2-3. 방문하지 않았다면
                queue.append(i) #2-4. 큐에 넣고
                visited[i] = True  #2-5. 방문처리하라!

dfs(graph, 1, visited)            

```

#### 문제풀이
배운 것
- 일단 bfs가 depth / 최단경로 등의 문제에 쓰인다는 것은 알겠음. 그 외의 상황에서는 좀 해봐야 알 듯? 뭐가 나을지?
- dfs / bfs가 이해는 되는데, 막상 문제에 적용하려니까 너무 빡셈...문제를 많이 풀어봐야 할 거 같음. 
- dfs는 재귀적 호출을 통해, bfs는 while을 통해 구현하는 경향이 있는듯?
- visited가 필수적인 것은 아니라는 점도 확인해 두면 좋을 듯. 
- 내일부터 greedy와 bfs / dfs문제 열심히 풀어보자.


----------------------------------------------------------------------
### Day14.
##### 20220606_백준_Greedy_보물, 설탕공장, ATM, 동전1.py
배운 것
- 3,5로 모두 나누는 Greedy의 경우, 5로 나누어질 때 까지 하나하나 3을 뺴고 5의 몫을 넣는 식으로 진행하면 됨. (순서가 직관과 반대임)



----------------------------------------------------------------------
### Day15.
##### 20220607_백준_DFS_DFS와 BFS.py
배운 것
- 일단 for에서 `_`의 쓰임
```
# 예를 들어 dfs / bfs 문제에서 graph에 대한 정보가 노드별로 연결된 형태가 아니라, 연결된 애들끼리 값을 주어서 변환하고 싶다면
# 그래서 노드개 + 1개의 빈 리스트를 만들고 싶다면

graph = [[] for _ in range(N+1)]
# 형태로 빈 리스트를 만들 수 있음. 이 때 이 반복문에서 index는 아무 쓸모가 없는 데, 이 때 쓰는 게 _라고. 

# 그래프를 완성하고 싶다면 
for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬. 작은 것부터 방문해야 하므로.
for i in range(len(graph)):
    graph[i].sort()
```
- 저 graph를 만드는 과정에서 sorting을 절대 잊지 말 것. 
- 그 외에 뭐...False * (N+1)이 아니라 [False] * (N+1)이라는 걸 헷갈리지 말 것 정도?

----------------------------------------------------------------------
### Day16.
##### 20220608_백준_BFS_단지번호붙이기.py
배운 것
- continue와 pass의 차이!
```
# pass는 실행할 것이 아무 것도 없다는 것을 의미한다. 사실상 없는 것과 차이가 없다
# continue는 다음 순번의 loop을 실행한다.

for i in range(1, 5):
    if i == 2:
        print("ready")
        pass
        print("go")
    print(i)

> 1
> ready
> go
> 2
> 3
> 4

for i in range(1, 5):
    if i == 2:
        print("ready")
        continue
        print("go")
    print(i)
> 1
> ready
> 3
> 4
```
- 그 외에 BFS / DFS는 좀 더 봐야 익숙해질듯

----------------------------------------------------------------------
### Day17.
##### 20220613_백준_BFS_바이러스.py
배운 것
- DFS / BFS를 위한 그래프 데이터를 만들 때, 나는 노드 별 connected 된 노드의 리스트가 있는 것이 좋다. 
- 이를 위해서는 아래의 코드를 사용해야 한다. 자연스럽게 쓸 수 있도록 숙달해두자.

```
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input.split())
    graph[a].append(b)
    graph[b].append(a)
```


----------------------------------------------------------------------
### Day18.
##### 20220614_백준_BFS_토마토.py
배운 것
- 이처럼 걸리는 시간 / 날짜를 구하는 문제는 BFS로 푸는 게 맞다. 
- 그 과정에서 graph의 값에 +1을 해가며 MAX를 구하는 식으로 구하자.
```
# 기존 BFS 코드에서 사용했던 것보다 더 효율적인 코드가 있어서 수정한다

# 기존
if nx < 0 or ny < 0 or nx >= N or ny >= M:
    continue
if graph[nx][ny] == 1:

# New
if 0<= nx < N and 0<= ny < M and graph[nx][ny] == 0:
```
- 진짜 M, N이 제일 헷갈린다. 정신 나갈 거 같음...

----------------------------------------------------------------------
### Day19.
##### 20220616_백준_BFS_연결요소의 개수.py
배운 것
- 그래프 만드는 코드에서 graph[a] = b가 아니라 graph[a].append(b)다. 헷갈리지 말자
- 아무것도 연결되어있지 않는 노드도 하나의 연결 요소다. 빼먹고 not graph조건을 까먹지 말자.
```
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면, 즉 지혼자 하나의 연결요소라면! 이거 까먹지 말자.
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(graph, i, visited)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다
```
----------------------------------------------------------------------
### Day20.
##### 20220621_타겟넘버, 프린터_Lv2.py
배운 것
- DFS, BFS는 단순히 예쁘게 노드와 노드 간의 연결을 나타낸 데이터만 쓸 수 있는 게 아님.
- visited같은 데이터가 없으면 아예 직접 idx를 만들어줘도 되는 것. 이탈조건만 잘 찾아준다면 말이지. 이런 응용 형태의 D/BFS문제 많이 풀어보자.
- 또 프로그래머스처럼 아예 solution을 함수 형태로 만들어야 한다면 함수 내부의 함수와 nonlocal을 잘 이용해보자
```
def solution(numbers, target):
    ans = 0
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal ans # 바로 이렇게, 보다 high level에서 지정된 변수를 업데이트할 때 사용가능.
                ans += 1
        else :
            dfs(idx +1, result + numbers[idx])
            dfs(idx +1, result - numbers[idx])
        return ans
    dfs(0,0)
    return ans  
```
----------------------------------------------------------------------
### Day21.
##### 20220623_타겟넘버_Lv2.py
배운 것
- sum()은 시간복잡도가 높다. loop에서 지속적으로 같은 자료를 sum 칠거라면 차라리 sum_of_list와 같은 객체를 만들어서 +=로 직접 할당하는 것이 훨씬 빠르다.
- 스택 / 큐 문제는 이제 한 두개만 더 풀고 피해가도 될 듯. 쉽네.
- 역시 문제는 DFS / BFS인듯.
----------------------------------------------------------------------
### Day22.
##### 20220627_백준_BFS_섬의_개수.py
배운 것
- 대각선을 간다? dx, dy를 8방향으로 수정하면 됨.
----------------------------------------------------------------------

### Day23.
##### 20220630_후보키_Lv2.py
배운 것
- set.discard는 엘리먼트가 없어도 정상적으로 종료함. remove와의 가장 큰 차이점!
- set에 들어가는 요소는 변형이 불가능해야 함. 그래서 list로 넣는 것이 아닌, tuple로 바꿔서 넣어줘야 함.
- itertools에서 combination / permutation 사용 가능
- collections에서 Counter를 사용 가능하고, Counter끼리 서로 + - 하면서 연산도 가능함. 이걸 사용하면 두 집단에 차이를 알 수도 있겠지.
- 차근히 풀었으면 풀 수 있는 문제였는데 너무 어렵게 생각한듯.
- Lv2 스킬체크 조만간 다시보자.

----------------------------------------------------------------------

### Day24.
##### 20220719_양궁대회_2xn타일링_Lv2.py
배운 것
- lv2 스킬체크 패스!
- 애매하면 그냥 loop을 돌리는 판단 좋았음. 근데 나중에는 이러면 안되겠지만...
- 결국에는 bfs또 이거임. 양궁대회는 bfs인지도 몰랐음;
- 더 풀어야지...백준으로 돌아갈 시간임.

----------------------------------------------------------------------

### Day...오랜만.
##### 깃허브 연동이 풀렸고...노트북은 다시 반납해야 하는 슬픈 미래
배운 것
- 선택 정렬 : 매번 처리하지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞의 값과 비교, 작다면 바꿔주는 것
- Python에서는 이중 반복문으로 선택 정렬을 구현할 수 있음
```
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
```
- N 번만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함. 즉 N번 정렬하고, n-1번 정렬하고... 따라서 등차수열의 함에 따라 O(N^2)의 시간 복잡도를 가짐
- 삽입 정렬 : 처리되지 않은 데이터를 하나 골라 적합한 위치에 삽입. 선택 정렬에 비해 구현이 좀 더 어렵지만, 좀더 보통 빠름.
- 첫 원소는 정렬이 되어있다고 판단하고, 두 번째 데이터가 첫 원소의 왼쪽인지 오른쪽인지 판단하는 것을 반복.
- 마찬가지로 이중 반복문으로 구현 가능.

```
for i in range(1, len(array)):
    for j in range(i, 0, -1)): # i부터 1까지 자리를 계속 바꿈
        if array[j] < array[j-1]: # 자기보다 크면 자리 바꾸면서 계속 이
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break # 자기보다 작으면 스탑
```
- 두 번 중첩되니 기본적으로 O(N^2)의 시간 복잡도를 가지나, 최선의 경우, 즉 거의 정렬이 된 경우 O(N)이 됨. 

- 퀵정렬 : 기준 데이터를 설정하고, 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 기본적인 퀵 정렬은 첫 데이터를 Pivot으로 기준데이터로 사용.
- 첫 번째 데이터를 기준으로 잡고, 왼쪽에서는 그보다 큰 값을, 오른쪽에서는 그보다 작은 값을 찾고 그 둘의 위치를 바꿈. 
- 반복함. 그러다가 왼쪽에서부터의 데이터와 오른쪽에서부터의 데이터의 위치가 엇갈렸을 경우, 작은 데아터와 피벗의 위치를 바꿈. 
- 이제 바꾼 데이터를 기준으로 왼쪽 / 오른쪽을 각각 정렬함. 
- 평균 O(NlogN)의 시간복잡도를 가짐.

```
def quick_sort(array, start, end):
    if start > = end:
        return
     pivot = start
     left = start + 1
     right = end
     
     while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 오른쪽은 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        
        # 엇갈렸다면, 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 아니라면 작은 데이터와 큰 데이터를 교체
        else:
            array[right], array[left] = array[left], array[right]
            
    # 분할 이후, 좌우에서 다시 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
```

- 좀 더 pythonic 하게 구현하면 아래와 같이 구현할 수 있음
```
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    # 분할 이후 각각 정렬 후 전체 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
```

- 계수정렬 : 특정 조건이 부합하면 아주 빠른 알고리즘. 데이터으 크기 범위가 정수 형태로 표현할 수 있을 때 사용
- 데이터의 개수가 N, 최대값이 K일 때, 최악의 경우에도 O(N+K)
- 가장 작은 데이터부터, 가장 큰 데이터까지 범위가 전부 담길 수 있도록 리스트 생성.
- 각각의 데이터가 속한 인덱스에 데이터가 몇 번씩 존재하는지를 확인해서, 그 위치의 계수를 증가시킴
- 그리고 그 인덱스에 해당하는 count만큼 그 인덱스를 출력하는 것. 

```
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count(i)):
        print(i, end = ' ')
```
- 때에 따라서 데이터의 범위가 너무 큰 경우는 제대로 작동하기 힘듦. 
- 반면 성적 같이, 해당 범위는 한정적이고 정렬할 값의 중복은 많은 경우 쓰기 좋음.

- 이진탐색 : 정렬된 데이터 대해, 아주 넓은 범위의 값을 반씩 짤라가면서 탐색하는 로직
```
from bisect import bisect_left, bisect_right

# bisect_left(array, x) : 정렬 유지하면서 array에 x를 삽입할 가장 왼쪽 index반환! right도 마찬가지.
```
- 입국심사 문제 다시 풀어보자
https://school.programmers.co.kr/questions/46032
