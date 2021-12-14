from typing import DefaultDict


def get_data():
    with open("input6.txt", "r") as input:
        for item in input:
            data = item.split(",")
        
        data[-1] = data[-1][:-1]
        for i in range(len(data)):
            data[i] = int(data[i])
        return(data)


def solve(fishes, iterations):
    count = 0
    tally = [0 for x in range(9)]
    for fish in fishes:
        tally[fish] +=1
    for i in range(iterations):
        spawning = tally[0]
        del tally[0]
        tally[6] += spawning
        tally.append(spawning)

    for x in tally:
        count += x

    return(str(count))





print("Day 6 Task 1 Answer: " + solve(get_data(), 80))
print("Day 6 Task 2 Answer: " + solve(get_data(), 256))

