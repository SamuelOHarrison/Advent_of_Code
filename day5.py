def get_data():
    data = []
    with open("input5.txt", "r") as input:
        for line in input:
            #seperate out all of the different x and y values into
            #the form [[x1,y1],[x2,y2]]
            line = line[:-1]
            x1 = line[:line.index(",")]
            line = line[line.index(",")+1:]
            y1 = line[:line.index(" ")]
            line = line[line.index(">")+2:]
            x2 = line[:line.index(",")]
            y2 = line[line.index(",")+1:]
            data.append([[x1,y1],[x2,y2]])  
    return data

def count_intersections(lines):
    #get intersecting bits
    count = 0
    for item in lines.values():
        if item > 1:
            count +=1
            
    return(count)

def gen_key(x,y):
    return(x + "," + y)


def add_to_dict(key, dict):
    try:
        dict[key] +=1 #increment value if key already exists
    except KeyError:
        dict[key] = 1 #create key if not already in dict

def solve1(data):
    lines = {}
    for x in data:
        #see if x is same
        if x[0][0] == x[1][0]:
            minimum = min(int(x[0][1]), int(x[1][1]))
            maximum = max(int(x[0][1]), int(x[1][1]))
            #loop through all y values
            for i in range(minimum, maximum+1):
                key = gen_key(x[0][0], str(i))
                add_to_dict(key, lines)
        #see if y is same
        elif x[0][1] == x[1][1]:
            minimum = min(int(x[0][0]), int(x[1][0]))
            maximum = max(int(x[0][0]), int(x[1][0]))
            for i in range(minimum, maximum+1):
                key = gen_key(str(i), x[0][1])
                add_to_dict(key, lines)
    
    return(lines)


def solve2(data):
    lines = solve1(data)
    for a in data:
        if a[0][0] != a[1][0] and a[0][1] != a[1][1]:
            min_x = min(int(a[0][0]), int(a[1][0]))
            max_x = max(int(a[0][0]), int(a[1][0]))
            min_y = min(int(a[0][1]), int(a[1][1]))
            max_y = max(int(a[0][1]), int(a[1][1]))
            #need to check if the y values need to increase as the x values do or decrease as the x values increase
            if (int(a[0][1]) < int(a[1][1]) and int(a[0][0]) < int(a[1][0])) or (int(a[0][1]) > int(a[1][1]) and int(a[0][0]) > int(a[1][0])):
                y = min_y
                ascending = True
            else:
                y = max_y
                ascending = False
            #loop from lowest x value to highest
            for i in range(min_x, max_x+1):
                key = gen_key(str(i), str(y))
                add_to_dict(key, lines)
                if ascending == False:
                    y -=1
                else:
                    y +=1
    return(lines)


data = get_data()
print(count_intersections(solve1(data)))
data2 = get_data()
print(count_intersections(solve2(data2)))

