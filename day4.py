data = []
with open("input4.txt", "r") as input:
    for line in input:
        data.append(line)
    n = data[0]
    del data[0:2]

numbers = n.split(",")
#get rid of \n in last item
numbers[-1] = numbers[-1][:-1]
print(numbers)

#separate into boards
boards = []
board = []
counter = 0
for i in data:
    line = i.split(" ")
    line[-1] = line[-1][:-1]
    for x in line:
        if x == "":
            line.remove("")
    if len(line) > 4:
        board.append(line)
        counter += 1
    if counter == 5:
        boards.append(board)
        board = []
        counter = 0

for x in numbers:
    for y in boards:
        pass

