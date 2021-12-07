def task1():
    horizontal_distance = 0
    depth = 0
    with open("input2.txt", "r") as input:
        for line in input:
            instruction = line[:line.index(" ")]
            distance = int(line[line.index(" "):])
            if instruction == "up":
                depth -= distance
            elif instruction == "down":
                depth += distance
            elif instruction == "forward":
                horizontal_distance += distance
    return(horizontal_distance*depth)

def task2():
    horizontal_distance = 0
    depth = 0
    aim = 0
    with open("input2.txt", "r") as input:
        for line in input:
            instruction = line[:line.index(" ")]
            distance = int(line[line.index(" "):])
            if instruction == "up":
                aim -= distance
            elif instruction == "down":
                aim += distance
            elif instruction == "forward":
                horizontal_distance += distance
                depth += aim*distance
    return(horizontal_distance*depth)

print(task1())
print(task2())