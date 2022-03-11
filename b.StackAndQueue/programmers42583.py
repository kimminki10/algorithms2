
def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [ 0 ] * bridge_length + truck_weights
    bridge_sum = sum(bridge[:bridge_length])

    while bridge:
        bridge_sum -= bridge.pop(0)
        if len(bridge) >= bridge_length: 
            bridge_sum += bridge[bridge_length-1]
            
        if bridge_sum > weight:
            bridge_sum -= bridge[bridge_length-1]
            bridge.insert(bridge_length-1, 0)
        answer += 1
    return answer 


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))
