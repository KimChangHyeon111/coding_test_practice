# My Ans
def solution(record):
    # 일단 uid의 list가 하나 필요하고
    # update가 가능한 id의 list가 필요해
    # dict로 만들고, Enter나 Change모두 update문으로 사용하면 되지 않을까?
    
    # uid - id를 이은 dictionary 생성
    answer = list(map(lambda x:x.split(), record))
    action_list = [i[0] for i in answer]
    uid_list = [i[1] for i in answer]
    uid_id_dict = dict(zip([i[1] for i in answer], [None]*len(uid_list)))
    for i in range(len(action_list)):
        if action_list[i] == 'Enter' or action_list[i] == 'Change':
            uid_id_dict.update({uid_list[i]:answer[i][2]})
        else:
            pass
    
    # result 반환        
    result = []     
    for info in record:
        if info.split()[0]=="Enter":
            result.append(uid_id_dict[info.split()[1]]+"님이 들어왔습니다.")
        elif info.split()[0]=="Leave":
            result.append(uid_id_dict[info.split()[1]]+"님이 나갔습니다.")    
    
    return result

# Top2 Ans
def solution(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]
# 미친 거 아니냐 진짜;;;

# Top1 Ans
def solution(record):
    answer = []
    id={info.split()[1]:info.split()[2] for info in record if info.split()[0]!="Leave"}
    for info in record:
        if info.split()[0]=="Enter":
            answer.append(id[info.split()[1]]+"님이 들어왔습니다.")
        elif info.split()[0]=="Leave":
            answer.append(id[info.split()[1]]+"님이 나갔습니다.")
    return answer
