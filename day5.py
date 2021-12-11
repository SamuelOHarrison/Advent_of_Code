def get_data():
    data = []
    with open("input5.txt", "r") as input:
        for line in input:
            line = line[:-1]
            x1 = line[:line.index(",")]
            line = line[line.index(",")+1:]
            y1 = line[:line.index(" ")]
            line = line[line.index(">")+2:]
            x2 = line[:line.index(",")]
            y2 = line[line.index(",")+1:]
            #print(x1,y1,x2,y2)
            data.append([[x1,y1],[x2,y2]])  
    return data


def solve1(data):
    lines = {}
    for x in data:
        #see if x is same
        if x[0][0] == x[1][0]:
            minimum = min(int(x[0][1]), int(x[1][1]))
            maximum = max(int(x[0][1]), int(x[1][1]))
            for i in range(minimum, maximum+1):
                key = x[0][0] + str(i)
                try:
                    lines[key] +=1
                except KeyError:
                    lines[key] = 1
        #see if y is same
        elif x[0][1] == x[1][1]:
            minimum = min(int(x[0][0]), int(x[1][0]))
            maximum = max(int(x[0][0]), int(x[1][0]))
            for i in range(minimum, maximum+1):
                key = str(i) + x[0][1]
                try:
                    lines[key] +=1
                except KeyError:
                    lines[key] = 1
    
    #get intersecting bits
    count = 0
    for item in lines.values():
        if item > 1:
            count +=1
            
    return(count)


data = get_data()
print(solve1(data))

