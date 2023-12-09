def find_first_num(line):
    for char in line:
        if char.isdigit():
            return char
    return None

def find_last_num(line):
    for char in reversed(line):
        if char.isdigit():
            return char
    return None

cali_sum = 0

with open("input.txt") as file:
    for line in file:
        tens = find_first_num(line)
        ones = find_last_num(line)
        full_value = str(tens) + str(ones)

        cali_sum += int(full_value)

print(cali_sum)



