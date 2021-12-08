def get_and_format_data():
    data = []
    with open("input4.txt", "r") as input:
        for line in input:
            data.append(line)
        n = data[0]
        del data[0:2]

    numbers = n.split(",")
    #get rid of \n in last item
    numbers[-1] = numbers[-1][:-1]

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
    
    return([boards, numbers])

def check_board(board):
    vertical = [0,0,0,0,0]
    vertical_bingo = False
    for line in board:
        horizontal = 0
        for num in line:
            if num[-1] == "x":
                horizontal +=1
                vertical[line.index(num)] += 1
    for x in vertical:
        if x == 5:
            vertical_bingo = True
    if horizontal == 5 or vertical_bingo == True:
        return(board)
    else:
        return False


def check_for_win(boards):
    indecies = []
    for board in boards:
        if check_board(board) != False:
            indecies.append(boards.index(board))
    if len(indecies) > 0:
        return(indecies)
    return (False)
        



def find_bingo(boards, numbers):
    winning_number = numbers[0]
    for x in numbers:
        winner = check_for_win(boards)
        if winner == False:
            for board in boards:
                for line in board:
                    for num in line:
                        if num == x:
                            num = num + "x"
                            winning_number = x
                            

        else:
            return([winner, winning_number])

def solve1(boards, winner, number):
    sum = 0
    for line in boards[winner[0]]:
        for num in line:
            if num[-1] != "x":
                sum += int(num)
    answer = sum*int(number)
    return(answer)

def solve2(boards, numbers):
    #get last board
    while len(boards) > 1 and len(numbers) > 0:
        winner = find_bingo(boards, numbers)
        for x in range(len(winner[0])-1, 0, -1):
            del boards[winner[0][x]]
        last_num = numbers[0]
        print(last_num)
        numbers = numbers[numbers.index(winner[1])+1:]

    
    print(boards)


    sum = 0
    for line in boards[0]:
        for num in line:
            if num[-1] != "x":
                sum += int(num)
    print(sum, last_num)
    answer = sum*int(last_num)
    return(answer)




data = get_and_format_data()
boards = data[0]
numbers = data[1]
winning_board_and_num = find_bingo(boards, numbers)
#print("Day 4 task 1 answer: " + str(solve1(boards, winning_board_and_num[0], winning_board_and_num[1])))
data = get_and_format_data()
boards = data[0]
print(boards)
numbers = data[1]
print("Day 4 task 2 answer: ", str(solve2(boards, numbers)))


