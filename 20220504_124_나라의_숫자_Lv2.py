# My Ans
# 효율성 테스트에서 1개 빼고 다 탈락
import math
def solution1(n):
    # 1) 등비수열의 합의 ...기준...아 설명하기 힘들다  아무튼 k 구하기
    k =math.floor(math.log(2*n+1,3)-1)

    # 2) 대충 공식에 따라 루프하기
    result = ""
    to_div = n- ((3**(k+1)-1)/2)
    while k >= 0:      
        decimal, to_div = divmod(to_div, 3**(k))
        result += str(int(decimal))
        k -= 1

    # 3) 치환하기
    result = result.replace('2','4')
    result = result.replace('1','2')
    result = result.replace('0','1')
    return result

# Top1 Ans
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

# Top2 Ans
def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]