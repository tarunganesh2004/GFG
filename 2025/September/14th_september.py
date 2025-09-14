# Gas Station

gas=[4,5,7,4]
cost=[6,6,3,5]


def canCompleteCircuit(gas,cost):
    n=len(gas)
    total_tank, curr_tank=0,0
    starting_station=0
    for i in range(n):
        total_tank+=gas[i]-cost[i]
        curr_tank+=gas[i]-cost[i]
        if curr_tank<0:
            starting_station=i+1
            curr_tank=0
    if total_tank>=0:
        return starting_station
    else:
        return -1
    
print(canCompleteCircuit(gas,cost))