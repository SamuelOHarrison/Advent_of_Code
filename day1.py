def day1_task1(input):
    previous_line = -1
    increase_count = 0
    for line in input:
        if previous_line != -1:
            if previous_line < int(line):
                increase_count +=1
            
        previous_line = int(line)
    return(increase_count)


def day1_task2(input):
    input_list = []
    increment_count = 0
    for line in input:
        input_list.append(int(line))
    for x in range(len(input_list)-3):
        sum1 = input_list[x] + input_list[x+1] + input_list[x+2]
        sum2 = input_list[x+1] + input_list[x+2] + input_list[x+3]
        if sum2 > sum1:
            increment_count += 1
    return(increment_count)


def solve():
    with open("input1.txt", "r") as input:
        day1_solved = day1_task1(input)
    with open("input1.txt", "r") as input:
        day2_solved = day1_task2(input)
    print("Task 1: " + str(day1_solved))
    print("Task 2: " + str(day2_solved))

        
solve()