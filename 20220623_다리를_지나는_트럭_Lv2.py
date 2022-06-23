# 먼저 들어간 트럭이 먼저 나와야 함 -> Queue로 풀면 될 듯?

from collections import deque

def solution1(bridge_length, weight, truck_weights):
    bridge_queue = deque([0] * (bridge_length-1)+[truck_weights[0]])
    waiting_queue = deque(truck_weights[1:len(truck_weights)])
    time = 1
    while waiting_queue:
        bridge_weight = sum(bridge_queue)
        bridge_out = bridge_queue.popleft()
        if bridge_weight+waiting_queue[0] < weight:
            new_truck = waiting_queue.popleft()
            bridge_queue.append(new_truck)
            time += 1
        else :
            bridge_queue.append(0)
            time += 1
    return time

def solution2(bridge_length, weight, truck_weights):
    bridge_queue = deque([0] * (bridge_length))
    waiting_queue = deque(truck_weights)
    time = 0
    while waiting_queue:
        bridge_out = bridge_queue.popleft()        
        bridge_weight = sum(bridge_queue)
        if bridge_weight+waiting_queue[0] <= weight:
            new_truck = waiting_queue.popleft()
            bridge_queue.append(new_truck)
            time += 1
        else :
            bridge_queue.append(0)
            time += 1
    return time+bridge_length

def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([0] * (bridge_length))
    waiting_queue = deque(truck_weights)
    bridge_weight = sum(bridge_queue)
    time = 0
    
    while waiting_queue:
        out = bridge_queue.popleft()
        bridge_weight -= out
        time += 1
        if bridge_weight+waiting_queue[0] <= weight:
            new_truck = waiting_queue.popleft()
            bridge_queue.append(new_truck)
            bridge_weight += new_truck
        else :
            bridge_queue.append(0)
    return time+bridge_length

