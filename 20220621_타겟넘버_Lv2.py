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