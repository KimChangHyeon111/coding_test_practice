# My Ans
def solution(lottos, win_nums):
    # 0의 개수. 전부 1이거나 전부 0이거나.
    poss_num = 0
    for i in lottos:
        poss_num += i == 0
    
    # 실제 match의 개수.
    isin = 0
    for i in lottos:
        isin += int(i in win_nums)
    
    result_max = 7 - (isin + poss_num)
    result_min = 7 - (isin)
    
    if result_min > 6:
        result_min = 6
    if result_max > 6:
        result_max = 6
        
    answer = [result_max, result_min]
    return answer

# Top1 Ans
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# Top2 Ans
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
