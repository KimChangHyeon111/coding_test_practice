# My Ans
import re
def solution(s): 
    s = str(s)
    s = re.sub('one','1',s)
    s = re.sub('two','2',s)
    s = re.sub('three','3',s)
    s = re.sub('four','4',s)
    s = re.sub('five','5',s)
    s = re.sub('six','6',s)
    s = re.sub('seven','7',s)
    s = re.sub('eight','8',s)
    s = re.sub('nine','9',s)
    s = re.sub('zero','0',s)
    return int(s)

# Top Ans
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
