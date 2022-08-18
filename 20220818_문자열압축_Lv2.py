# 나의 풀이
def solution(s):    
    # string_list : 나눌 candidate으로 쪼개서 모은 String들의 리스트
    string_list = []
    for candidate in range(1,len(s)+1):        
        strings = [s[i:i+candidate] for i in range(0,len(s),candidate)]            
        string_list.append(strings)
    
    # cnt_list : 최종 길이 cnt들을 모은 리스트 
    cnt_list = []
    for strings in string_list:
        current_s = strings[0]
        cnt = [len(current_s)]
        match = 0
        for string in strings[1:]:
            if string != current_s:
                cnt.append(len(string))
                current_s = string
                match = 0
            elif string == current_s :
                if match == 0:
                    cnt.append(1)
                    match += 1
                else :
                    match += 1
                    cnt.append(len(str(match+1)) - len(str(match)))
                
        cnt_list.append(sum(cnt))
        result = min(cnt_list)
    return result

# 고수의 풀이
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

# 이상하다 같은 로직인데 왜 내 코드는 이따구지...