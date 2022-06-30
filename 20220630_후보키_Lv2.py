from itertools import combinations
def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    
    idx_list = []
    for i in range(1,cols+1):
        idx_list.extend(combinations(range(cols),i))
    
    unique_key_list = []
    for i in idx_list:
        key = [tuple([item[key] for key in i]) for item in relation]
        if len(set(key)) == rows:
            unique_key_list.append(i)
    
    result = set(unique_key_list)
    for i in range(len(unique_key_list)):
        for j in range(i+1, len(unique_key_list)):
            if len(unique_key_list[i]) == len(set(unique_key_list[i]) & set(unique_key_list[j])):
                result.discard(unique_key_list[j])
                
    return len(result)

# set이나 딕셔너리의 키의 원소는 해시할 수 있는 "변형이 불가능한" (immutable) 값이어야 한다. 그래서 셋에 리스트를 넣을 수 없는것!