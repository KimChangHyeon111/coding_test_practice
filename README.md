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
