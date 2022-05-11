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
