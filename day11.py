from typing import DefaultDict


def get_data(filename):
    with open(filename, "r") as input:
        data = []
        for line in input:
            line = line[:-1]
            new_line = []
            for item in line:
                new_line.append(int(item))
            data.append(new_line)

    print(data)
    return(data)

def increment_octopi(data):
    for y in range(10):
        for x in range(10):
            data[y][x] += 1

def flash(y,x,data,flashed):
    for y2 in range(y-1, y+2):
        for x2 in range(x-1, x+2):
            if y2 >= 0 and x2 >= 0 and y2 < 10 and x2 < 10:
                data[y2][x2] +=1
                if data[y2][x2] > 9 and str(y2)+","+str(x2) not in flashed:
                    flashed[str(y2) + "," + str(x2)] = True
                    flash(y2,x2,data,flashed)


def flashes(data):
    flashed = DefaultDict()
    for y in range(10):
        for x in range(10):
            if data[y][x] > 9 and str(y)+","+str(x) not in flashed:
                data[y][x] += 1
                flashed[str(y) + "," + str(x)] = True
                flash(y,x,data,flashed)
    
    return(len(flashed))

def set_flashed_to_0(data):
    for y in range(10):
        for x in range(10):
            if data[y][x] > 9:
                data[y][x] = 0

def solve1(data):
    flashes_count = 0
    for i in range(100):
        increment_octopi(data)
        flashes_count += flashes(data)
        set_flashed_to_0(data)

    return(str(flashes_count))


def solve2(data):
    all_flashed = False
    step = 0
    while all_flashed == False:
        increment_octopi(data)
        no_flashes = flashes(data)
        set_flashed_to_0(data)
        if no_flashes == 100:
            all_flashed = True
        step += 1
    
    return(str(step))


print("Day 11 Task 1 Answer: " + solve1(get_data("input11.txt")))
print("Day 11 Task 2 Answer: " + solve2(get_data("input11.txt")))