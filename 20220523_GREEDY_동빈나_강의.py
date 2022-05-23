#1260원을 거슬러 주는 알고리즘을 만든다고 하면

n = 1260
ct = 0

coin = [500,100,50,10]

for c in coin:
    ct += n//c # 그 화폐로 거슬러 줄 수 있는 최대의 숫자
    n %= c        # 거슬러 준 나머지
    
print(c)

# 1이 될 때 까지
# N이 1이 될 때까지 1을 빼고, K로 나누어떨어지면 K로 나눔
# 이 때 빼거나, 나누는 최소 횟수를 구하라

# 이건 일단 나누고, 못 나누면 빼는 Greedy알고리즘으로 작성하면 됨. 


n, k = map(int, input().split())

result = 0

while True:
    # N이 나누어 떨어질 때 까지 빼기
    target = (n//k)*k # 나누어 떨어지는 가장 큰 n을 타겟에 할당
    result += (n - target) # 그 차를 구하면 그게 바로 1을 빼는 횟수
    n = target # 다시 반복
    if n < k: # 나눌 숫자보다 작아지면, 즉 더는 나눌 수 없어지면 반복문 탈출
        break
    result += 1
    n //= k # 그게 아니면 k로 나눠서 다시 loop
result += (n-1) # n이 1보다 크면 1로 만들어야 하니까 그만큼 빼는 연산을 또 한번에 처리한 샘
print(result)    

# 곱하기 또는 더하기
# 각 자리가 0~9로만 이뤄진 문자열 S가 주어졌을 때, 왼쪽부터 확인하며 연산자를 넣어 만들어질 수 있는 가장 큰 수를 구하라
# 단 왼쪽부터 순서대로 이뤄진다. 
# 마찬가지로 일단 곱할 수 있으면 다 곱하는 Greedy문제

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else 
        result *= num

print(result)        


# 모험가 길드
# N명의 모험가가 있는데, 그들은 공포도가 있음. 
# 공포도가 X인 모험가는 X명 이상인 모험가 그룹에 참여해야 함
# N개의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최대값을 구하라. (단 다 갈 필요는 없다)

# 오름차순으로 정렬하고, 현재 그룹에 포험된 모험가 수가 확인하고 있는 모험가의 공포도보다 크거나 같으면 그룹으로 설정하면 됨. 

n = int(input())
data = list(map(int, input().split()))
data.sort # 정렬

result = 0 # 그룹 수
count = 0 # 그룹에 포함된 모험가 수

for i in data:
    count += 1
    if count >= i: # 현재 그룹의 모험가의 수가 현재의 공포도 이상이면 그룹 결성
        result += 1
        count = 0

print(result)
