def get_data(filename):
    data = [] # Will be 2d array with each sub array being a line
    # this will mean the indexing will be in the form data[y][x]
    with open(filename, "r") as input:
        for line in input:
            line = line[:-1]
            new_line = []
            for x in line:
                new_line.append(x)
            data.append(new_line)
    return(data)

def check_hotspot(y, x, data):
    point = int(data[y][x])
    hotspot = True
    for c in [[1,0],[0,1],[-1,0],[0,-1]]:
        if y+c[0] <= len(data)-1 and x+c[1] <= len(data[0])-1 and y+c[0] >= 0 and x+c[1] >= 0:
            if point >= int(data[y+c[0]][x+c[1]]):
                hotspot = False
        else:
            continue
        

    return hotspot



def solve1(data):
    output = 0
    for y in range(len(data)):
        for x in range(len(data[1])):
            hotspot = check_hotspot(y, x, data)
            if hotspot != False:
                output += int(data[y][x])+1

    return(str(output))

def explore(y,x, data, basin):
    point = int(data[y][x])
    for c in [[1,0],[0,1],[-1,0],[0,-1]]:
        if y+c[0] <= len(data)-1 and x+c[1] <= len(data[0])-1 and y+c[0] >= 0 and x+c[1] >= 0:
            comparing_point = int(data[y+c[0]][x+c[1]])
            if comparing_point > point and comparing_point != 9 and comparing_point not in basin:
                basin[str(y+c[0])+ "," + str(x+c[1])] = True
                explore(y+c[0], x+c[1], data, basin)
    return 0
                

    

def solve2(data):
    basin_sizes = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            possible_hotspot = check_hotspot(y, x, data)
            if possible_hotspot != False:
                basin = {str(y)+","+str(x): True}
                explore(y, x, data, basin) # recursive function to explore all neighbours that are higher
                basin_sizes.append(len(basin)) # the basin dict will always ensure no node is explored twice and the length will be all explored nodes
    basin_sizes.sort()
    print(basin_sizes)
    product = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3] 
    return str(product)

print("Day 9 Task 1 Answer: " + solve1(get_data("input9.txt")))
print("Day 9 Task 2 Answer: " + solve2(get_data("input9.txt")))