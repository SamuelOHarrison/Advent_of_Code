def get_data(filename):
    #reuturn a list of all crab positions
    with open(filename, "r") as input:
        for item in input:
            data = item.split(",")
        
        data[-1] = data[-1][:-1]
        for i in range(len(data)):
            data[i] = int(data[i])  
    return(data)

def get_fuel_cost(crabs, point):
    fuel_cost = 0
    for crab in crabs:
        fuel_cost += abs(crab - point)
    return(fuel_cost)

def get_fuel_cost_2(crabs, point):
    fuel_cost = 0
    for crab in crabs:
        initial_cost = abs(crab - point)
        sum_to = (initial_cost*(initial_cost+1))//2
        fuel_cost += sum_to
    return(fuel_cost)


def solve1(crabs):
    min = crabs[0]
    max = crabs[0]
    for x in crabs:
        if x < min:
            min = x
        if x > max:
            max = x
    lowest_fuel_cost = get_fuel_cost(crabs, 0)
    for x in range(min,max+1):
        fuel_cost = get_fuel_cost(crabs, x)
        if fuel_cost < lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost
    
    return(str(lowest_fuel_cost))

def solve2(crabs):
    min = crabs[0]
    max = crabs[0]
    for x in crabs:
        if x < min:
            min = x
        if x > max:
            max = x
    lowest_fuel_cost = get_fuel_cost_2(crabs, 0)
    for x in range(min,max+1):
        fuel_cost = get_fuel_cost_2(crabs, x)
        if fuel_cost < lowest_fuel_cost:
            lowest_fuel_cost = fuel_cost
    
    return(str(lowest_fuel_cost))


print("Day 7 Task 1 Answer: " + solve1(get_data("input7.txt")))
print("Day 7 Task 2 Answer: " + solve2(get_data("input7.txt")))
