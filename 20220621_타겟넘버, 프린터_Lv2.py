from collections import deque

# BFS
def solution(numbers, target):
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([numbers[0]*-1,0])
    result = 0
    while queue:
        number, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):
            queue.append([number - numbers[idx],idx])
            queue.append([number + numbers[idx],idx])
        else:
            if number == target:
                result += 1
    return result


# DFS
def solution(numbers, target):
    ans = 0
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal ans
                ans += 1
        else :
            dfs(idx +1, result + numbers[idx])
            dfs(idx +1, result - numbers[idx])
        return ans
    dfs(0,0)
    return ans    


from collections import deque

def solution(priorities, location):
    idx = deque(range(len(priorities)))
    queue = deque(priorities)
    
    result = []
    result_idx = []
    
    while len(queue)>1 :
        pop = queue.popleft()
        pop_idx = idx.popleft()
        if pop >= max(queue):
            result.append(pop)
            result_idx.append(pop_idx)
        else:
            queue.append(pop)
            idx.append(pop_idx)
            
    result.append(queue.popleft())
    result_idx.append(idx.popleft())
    return result_idx.index(location)+1