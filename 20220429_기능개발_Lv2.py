#My Ans
import numpy as np
def solution(progresses, speeds):
    res_load = (np.array([100]*len(progresses)) - np.array(progresses))
    res_d = np.ceil(res_load/np.array(speeds)).tolist()
    
    ct_list =[]
    comp1 = res_d[0]
    i = 1
    ct = 1
    
    while i < len(res_d):
        if comp1 >= res_d[i]:
            i += 1
            ct += 1
        else:
            ct_list.append(ct)                        
            comp1 = res_d[i]
            i += 1
            ct = 1
            
    ct_list.append(ct)            
    return ct_list

#Top1 Ans
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

