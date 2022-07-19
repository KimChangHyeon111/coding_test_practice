# 2Xn 타일링
def solution(n):
    t =[0 for i in range(n)]
    t[0], t[1] = 1,2
    for i in range(2,n):
        t[i] = (t[i-1] + t[i-2]) % 1000000007

    return t[n-1]

# 양궁대회
# 다 세어보는 나의 풀이
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = -55
    pos_result = list(combinations_with_replacement(range(0,11),n))

    for result in pos_result:
        r_shot = [0] * 11
        a_score = 0
        r_score = 0
        for score in result:
            r_shot[10-score] += 1

        for i in range(11):
            if info[i] == r_shot[i] == 0 :
                continue
            elif info[i] >= r_shot[i]:
                a_score += 10-i
            else:
                r_score += 10-i

        if r_score > a_score:
            if r_score - a_score  > max_diff:
                max_diff = r_score - a_score 
                answer = r_shot

    return answer


# 선주님의 풀이 (bfs)
# 솔직히 잘 이해가 안가니 나중에 다시보자
# https://velog.io/@hygge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-2022-KAKAO-BLIND-RECRUITMENT-BFS
from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear()
                res.append(arrow)  # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]
