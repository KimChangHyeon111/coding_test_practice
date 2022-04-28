#My Ans
def solution(a, b):
    zip1 = zip(a,b)
    result = [int(key) * value for key, value in zip1]
    rr = sum(result)
    return rr

#Top1 Ans
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
