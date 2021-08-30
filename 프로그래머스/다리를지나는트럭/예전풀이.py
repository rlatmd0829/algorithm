def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_ing = [0] * bridge_length
    while truck_ing:
        time += 1
        truck_ing.pop(0)
        if truck_weights:
            if sum(truck_ing)+truck_weights[0] <= weight:
                truck_ing.append(truck_weights.pop(0))
            else:
                truck_ing.append(0)
        
    return time