symbol_list = {'*'}

class Item:
    def __init__(self, x, y, value = None):
        self.value = value
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Am I a value? " + str(self.value)

def check_up(y_coord_list, x_coord):
    number_set = {}

    # Directly above could be a number, a symbol, or a dot
    up_val = y_coord_list[x_coord].value 
    if up_val == None:
        number_set[x_coord] = "."
    else:
        number_set[x_coord] = up_val
    
    temp_x_coord = x_coord
    while temp_x_coord - 1 > -1 and y_coord_list[temp_x_coord - 1] in y_coord_list.values() and y_coord_list[temp_x_coord - 1].value != None:
        number_set[temp_x_coord - 1] = y_coord_list[temp_x_coord - 1].value 
        temp_x_coord -= 1
    
    temp_x_coord_for = x_coord
    while temp_x_coord_for + 1 < 140 and y_coord_list[temp_x_coord_for + 1] in y_coord_list.values() and y_coord_list[temp_x_coord_for + 1].value != None:
        number_set[temp_x_coord_for + 1] = y_coord_list[temp_x_coord_for + 1].value
        temp_x_coord_for += 1
 
    sorted_dict = dict(sorted(number_set.items()))

    int_string = ""
    for value in sorted_dict.values():
        int_string += str(value)
    
    result = int_string.split(".")

    if len(result) > 0:
        return result
    else:
        return []    


def check_down(y_coord_list, x_coord): 
    number_set = {}

    # Directly below could be a number, a symbol, or a dog
    down_val = y_coord_list[x_coord].value 

    if down_val == None:
        number_set[x_coord] = "."
    else:
        number_set[x_coord] = down_val
    
    temp_x_coord = x_coord
    while temp_x_coord - 1 > -1 and y_coord_list[temp_x_coord - 1] in y_coord_list.values() and y_coord_list[temp_x_coord - 1].value != None:
        number_set[temp_x_coord - 1] = y_coord_list[temp_x_coord - 1].value 
        temp_x_coord -= 1

    temp_x_coord_for = x_coord
    while temp_x_coord_for + 1 < 140 and y_coord_list[temp_x_coord_for + 1] in y_coord_list.values() and y_coord_list[temp_x_coord_for + 1].value != None:
        number_set[temp_x_coord_for + 1] = y_coord_list[temp_x_coord_for + 1].value
        temp_x_coord_for += 1

    sorted_dict = dict(sorted(number_set.items()))

    int_string = ""
    for value in sorted_dict.values():
        int_string += str(value)
    
    result = int_string.split(".")

    if len(result) > 0:
        return result
    else:
        return []    

def check_left(y_coord_list, x_coord):
    number_set = {}

    if y_coord_list[x_coord - 1] not in y_coord_list.values():
        return []
    elif y_coord_list[x_coord - 1].value == None:
        return []
    else:
        temp_x_coord = x_coord
        while temp_x_coord - 1 > -1 and y_coord_list[temp_x_coord - 1] in y_coord_list.values() and y_coord_list[temp_x_coord - 1].value != None:
            number_set[temp_x_coord - 1] = y_coord_list[temp_x_coord - 1].value 
            temp_x_coord -= 1
        
        sorted_dict = dict(sorted(number_set.items()))
        int_string = ""
        for value in sorted_dict.values():
            int_string += str(value)
        
        return [int_string]

def check_right(y_coord_list, x_coord):
    number_set = {}

    if y_coord_list[x_coord + 1] not in y_coord_list.values():
        return []
    elif y_coord_list[x_coord + 1].value == None:
        return []
    else:
        temp_x_coord = x_coord
        while y_coord_list[temp_x_coord + 1] in y_coord_list.values() and y_coord_list[temp_x_coord + 1].value != None:
            number_set[temp_x_coord + 1] = y_coord_list[temp_x_coord + 1].value 
            temp_x_coord += 1
        
        sorted_dict = dict(sorted(number_set.items()))
        int_string = ""
        for value in sorted_dict.values():
            int_string += str(value)
        
        return [int_string]

def main():
    line_num = 0
    larger_dict = {}
    char_list = []
    sum_parts = 0

    with open("input.txt") as file:
        for line in file:
            larger_dict[line_num] = {}
            for ind, char in enumerate(line):
                if char in symbol_list:
                    larger_dict[line_num][ind] = Item(ind, line_num)
                    char_list.append(larger_dict[line_num][ind])
                elif char == '.':
                    larger_dict[line_num][ind] = Item(ind, line_num)
                elif char == '\n':
                    next
                else:
                    larger_dict[line_num][ind] = Item(ind, line_num, int(char))
            line_num += 1
        
        for symbol in char_list:
            if symbol.y > 0:
                val_u = check_up(larger_dict[symbol.y - 1], symbol.x)
            else:
                val_u = []

            if symbol.y < (line_num - 1):
                val_d = check_down(larger_dict[symbol.y + 1], symbol.x)
            else: 
                val_d = []

            val_l = check_left(larger_dict[symbol.y], symbol.x)
            val_r = check_right(larger_dict[symbol.y], symbol.x)
        
            val_u.extend(val_d)
            val_u.extend(val_l)
            val_u.extend(val_r)
            val_u.remove('')

            if len(val_u) == 2:
                sum = int(val_u[0]) * int(val_u[1])
            else:
                sum = 0
            
            sum_parts += sum
        
        print(sum_parts)


if __name__ == "__main__":
    main()
