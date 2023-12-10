symbol_list = {'@', '#', '$', '%', '&', '*', '=', '+', '/'}

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
    while y_coord_list[temp_x_coord_for + 1] in y_coord_list.values() and y_coord_list[temp_x_coord_for + 1].value != None:
        number_set[temp_x_coord_for + 1] = y_coord_list[temp_x_coord_for + 1].value
        temp_x_coord_for += 1
 
    sorted_dict = dict(sorted(number_set.items()))
    print(sorted_dict)

    int_string = ""
    for value in sorted_dict.values():
        print(value)
        int_string += str(value)
    
    result = int_string.split(".")

    total_up = 0
    for item in result:
        if item == "":
            next
        else:
            total_up += int(item)

    return total_up


def check_down(y_coord_list, x_coord): 
    down = 0
    diag_ld = 0
    diag_rd = 0
    #down, diag_ld, diag_rd
    return 1

def check_left(y_coord_list, x_coord):
    left = 0
    #left
    return 1

def check_right(y_coord_list, x_coord):
    right = 0
    #right
    return 1

def main():
    line_num = 0
    larger_dict = {}
    char_list = []
    sum_parts = 0


    # Read lines into unique item
    ## Each line is a dictionary
    ## Key in larger_dict is y-coordinate 
    ### Key should be x-coordinate, y is item value
    #### Example { 0: { 1: Item, 2: Item}, 1: {1: Item, 2: Item}}
    # with open("small_input.txt") as file:
    file = ["467..114..", "...*......"]
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
            up = check_up(larger_dict[symbol.y - 1], symbol.x)
        else:
            up = 0

        if symbol.y < (line_num - 1):
            down = check_down(larger_dict[symbol.y + 1], symbol.x)
        else: 
            down = 0

        
        left = check_left(larger_dict[symbol.y], symbol.x)
        right = check_right(larger_dict[symbol.y], symbol.x)

        sum_parts += up + down + left + right
    
    print(sum_parts)




                
    





    ## String concatination

    

if __name__ == "__main__":
    main()
