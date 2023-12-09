Text_Values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_endiest_num(list):
    if len(list) == 1:
        return list[0]
    else:
        greatest_ind = -1
        for element in list:
            if element[0] > greatest_ind:
                greatest_ind = element[0]
                list_return = element

        return list_return

def get_firstest_num(list):
    if len(list) == 1:
        return list[0]
    else:
        lowest_ind = 1000
        for element in list:
            if element[0] < lowest_ind:
                lowest_ind = element[0]
                list_return = element

        
        return list_return


def find_first_text_num(line):
    empty_list = []
    for item in Text_Values:
        if item in line:
            empty_list.append([line.index(item), Text_Values.get(item)])

    if not empty_list:
        return None, None
    else:
        index_value = get_firstest_num(empty_list)
        return index_value[0], index_value[1]

def find_last_text_num(line):
    empty_list = []
    for item in Text_Values:
        index = line.rfind(item)
        if index != -1:
            empty_list.append([index, Text_Values.get(item)])
        
    if not empty_list:
        return None, None
    else:
        index_value = get_endiest_num(empty_list)
        return index_value[0], index_value[1]
    
def find_first_num(line):
    for char in line:
        if char.isdigit():
            return line.index(char), char
    return None, None

def find_last_num(line):
    for char in reversed(line):
        if char.isdigit():
            return line.rfind(char), char
    return None, None

def get_tens(find, fval, fcind, fcval):
    if find is None:
        return fcval
    elif fcind is None:
        return fval
    else:
        return fval if find < fcind else fcval

def get_ones(lind, lval, lcind, lcval):
    if lind is None:
        return lcval
    elif lcind is None:
        return lval
    else:
        return lval if lind > lcind else lcval

cali_sum = 0

with open("input.txt") as file:
    for line in file:
        ftext_ind, ftext_val = find_first_text_num(line)
        ltext_ind, ltext_val = find_last_text_num(line)
        fchar_ind, fchar_val = find_first_num(line)
        lchar_ind, lchar_val = find_last_num(line)

        tens = get_tens(ftext_ind, ftext_val, fchar_ind, fchar_val)
        ones = get_ones(ltext_ind, ltext_val, lchar_ind, lchar_val)

        full_value = str(tens) + str(ones)

        cali_sum += int(full_value)

# ftext_ind, ftext_val = find_first_text_num("4sevens34")
# ltext_ind, ltext_val = find_last_text_num("4sevens34")
# fchar_ind, fchar_val = find_first_num("4sevens34")
# lchar_ind, lchar_val = find_last_num("4sevens34")

# tens = get_tens(ftext_ind, ftext_val, fchar_ind, fchar_val)
# ones = get_ones(ltext_ind, ltext_val, lchar_ind, lchar_val)

# full_value = str(tens) + str(ones)

# cali_sum += int(full_value)


print(cali_sum)


