# My Ans
import re
def make_items(str_value):
    str_value = str_value.lower()
    str1_list = [str_value[i-1]+str_value[i] for i in range(1,len(str_value))]
    tmp =[]
    for i in range(len(str1_list)):
        temp = re.findall(r'[a-zA-Z]', str1_list[i])
        if len(temp) == 2:
            tmp.append(temp[0]+temp[1])
    return tmp            

def get_intersect_list(list1, list2):
    result = []
    for i in list1:
        if i in list2:
                list2.remove(i)
                result.append(i)
    return result

def solution(str1, str2):
    if str1 == "" and str2 == "":
        answer = 65536
        str1_list  = ['0']
        str2_list = ['0']
        union = []
        intersection = []
    else :
        str1_list = make_items(str1)
        str2_list = make_items(str2)
        intersection = get_intersect_list(str1_list, str2_list)
        union = str1_list+str2_list
        if len(union) == 0:
            answer = 65536
        else :
            answer = len(intersection)/len(union) * 65536 // 1
    return answer#union, intersection

# Top1 Ans
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
