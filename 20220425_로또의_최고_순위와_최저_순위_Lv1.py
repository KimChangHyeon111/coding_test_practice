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