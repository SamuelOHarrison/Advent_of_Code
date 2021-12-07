def task1(): 
    counts1 = [0,0,0,0,0,0,0,0,0,0,0,0] #stores each bit count for 1
    counts0 = [0,0,0,0,0,0,0,0,0,0,0,0] #stores each bit count for 0
    with open("input3.txt", "r") as input:
        for line in input:
            for x in range(len(line)-1):
                if line[x] == "1":
                    counts1[x] += 1
                else:
                    counts0[x] += 1
    gamma = 0
    epsilon = 0
    for x in range(len(counts0)):
        if counts0[x] > counts1[x]:
            epsilon += 2**(11-x)
        else:
            gamma += 2**(11-x)

    print(gamma*epsilon)

def get_highest_bit_count(input, index):
    count1 = 0
    count0 = 0
    for x in input:
        if x[index] == "1":
            count1 += 1
        elif x[index] == "0":
            count0 += 1
        else:
            pass
    if count0 == count1:
        print("EQUAL")
    if count0 > count1:
        return "0"
    else:
        return "1"

def convert_to_dec(binary_num):
    dec_num = 0
    for x in range(len(binary_num)):
        if binary_num[x] == "1":
            dec_num += 2**(11-x)
    return dec_num


def task2(ox_or_co2):
    input_list = []
    with open("input3.txt", "r") as input:
        for line in input:
            input_list.append(line)
    index = 0
    while len(input_list) > 1:
        counter = 0
        msb = get_highest_bit_count(input_list, index)
        while counter < len(input_list):
            if input_list[counter][index] == msb:
                if ox_or_co2 == "ox":
                    counter +=1
                else:
                    del input_list[counter]
            else:
                if ox_or_co2 == "co2":
                    counter +=1
                else:
                    del input_list[counter]
        index += 1
    return (convert_to_dec(input_list[0]))




oxygen = task2("ox")
co2 = task2("co2")
print(oxygen*co2)