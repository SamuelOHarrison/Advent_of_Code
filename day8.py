from io import StringIO


def get_data(filename):
    data = []
    with open(filename, "r") as input:
        for line in input:
            line = line[:-1]
            data.append(line.split(" "))
        
    return(data)


def solve1(data):
    count = 0
    for line in data:
        bar_index = line.index("|")
        for i in range(bar_index, len(line)):
            if len(line[i]) in [2,3,4,7]:
                count += 1

    return(str(count))

def compare_to_4(string, line):
    for x in line:
        if len(x) == 4:
            four = x
            break
    count = 0
    for y in string:
        if y in four:
            count += 1
    
    return count

def compare_to_1(string, line):
    for x in line:
        if len(x) == 2:
            one = x
    count = 0
    for y in string:
        if y in one:
            count += 1

    return count

def compare(line, numbers, target):
    for x in numbers:
        comparison = compare_to_4(x, line) # returns the number of common letters
        if comparison == 4 and target == 9:
                return x
        elif target in [0,6] and comparison == 3:
            comp_one = compare_to_1(x, line)
            if comp_one == 1 and target == 6:
                return x
            elif comp_one == 2 and target == 0:
                return x
        elif comparison == 2 and target == 2:
                return x
        elif target in [3,5] and comparison == 3:
            comp_one = compare_to_1(x, line)
            if comp_one == 1 and target == 5:
                return x
            elif comp_one == 2 and target == 3:
                return x




def solve2(data):
    final_output = 0
    for line in data:
        five = []
        six = []
        bar_index = line.index("|")
        for i in range(bar_index):
            #2,3,5 all have string length 5
            if len(line[i]) == 5:
                if line[i] not in five:
                    five.append(line[i])
            #0,6,9 all have string length 6
            if len(line[i]) == 6:
                if line[i] not in six:
                    six.append(line[i])


        two = sorted(compare(line, five, 2))
        three = sorted(compare(line, five, 3))
        five = sorted(compare(line, five, 5))
        zero = sorted(compare(line, six, 0))
        nine = sorted(compare(line, six, 9))
        six = sorted(compare(line, six, 6))

        #all numbers now known
        output = ""
        for i in range(bar_index+1, len(line)):
            line[i] = sorted(line[i])
            if len(line[i]) == 2:
                output += "1"
            elif len(line[i]) == 3:
                output += "7"
            elif len(line[i]) == 4:
                output += "4"
            elif len(line[i]) == 7:
                output += "8"
            elif line[i] == zero:
                output += "0"
            elif line[i] == two:
                output += "2"
            elif line[i] == three:
                output += "3"
            elif line[i] == five:
                output += "5"
            elif line[i] == six:
                output += "6"
            elif line[i] == nine:
                output += "9"
            
        final_output += int(output)
    
    return(str(final_output))


print("Day 8 Task 1 Answer: " + solve1(get_data("input8.txt")))
print("Day 8 Task 2 Answer: " + solve2(get_data("input8.txt")))
