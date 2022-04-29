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
