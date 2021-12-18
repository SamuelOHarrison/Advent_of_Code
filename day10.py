from typing import final


def get_data(filename):
    data = []
    with open(filename, "r") as input:
        for line in input:
            line = line[:-1]
            data.append(line)
    return(data)



def get_syntax_score(line):
    closers = ["]", "}", ")", ">"]
    scores = [57, 1197, 3, 25137]
    openers = ["[", "{", "(", "<"]
    stack = []
    for x in range(len(line)):
        if line[x] in openers:
            stack.append(line[x])
        elif line[x] in closers:
            if openers.index(stack.pop()) == closers.index(line[x]):
                continue
            else:
                return(scores[closers.index(line[x])])
            




def solve1(data):
    sum = 0
    task2_input = []
    for line in data:
        score = get_syntax_score(line)
        if score is not None:
            sum += score
        else:
            task2_input.append(line)
        
    return ([str(sum),task2_input])

def solve2(data):
    openers = ["[", "{", "(", "<"]
    closers = ["]", "}", ")", ">"]
    scores = [2, 3, 1, 4]
    final_scores = []
    for line in data:
        stack = []
        score = 0
        for x in line:
            if x in openers:
                stack.append(x)
            elif x in closers:
                if openers.index(stack.pop()) == closers.index(x):
                    continue
        for i in range(len(stack)):
            score = score * 5
            top = stack.pop()
            score += scores[openers.index(top)]
        
        final_scores.append(score)
    
    final_scores.sort()
    middle_index = len(final_scores)//2

    
    return(str(final_scores[middle_index]))
            





print("Day 10 Task 1 Answer: " + solve1(get_data("input10.txt"))[0])
print("Day 10 Task 2 Answer: " + solve2(solve1(get_data("input10.txt"))[1]))