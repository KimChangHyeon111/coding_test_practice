# My Ans1 - Wrong / too slow
def solution1(scoville, K):
    n_iters = 0
    try:
        while sum([int(value >= K) for value in scoville]) < len(scoville):
            comp1 = min(scoville)
            scoville.remove(comp1)
            comp2 = min(scoville)
            scoville.remove(comp2)
            scoville = [comp1+2*comp2] + scoville
            print(scoville)
            n_iters += 1
    except:
        n_iters = -1
    return n_iters

# My Ans2 - Good. Using Heapq
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    n_iters = 0
    min1 = heapq.heappop(scoville)
    try:
        while min1 < K:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1+2*min2)
            n_iters += 1
            min1 = heapq.heappop(scoville)
    except:
        n_iters = -1
    return n_iters

# Top1 Ans
import heapq as hq
def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
