def find_color(colors, search):
    highest = 0
    for instance in colors:
        if search in instance:
            val = int(instance.split(" ")[0])

            if val > highest:
                highest = val

    return highest


def get_power(game):
    id, games = game.split(": ")
    lines = games.split("; ")

    colors = [] 

    for item in lines:
        foo = item.split(", ")
        colors.extend(foo)
    
    

    red = find_color(colors, "red")
    green = find_color(colors, "green")
    blue = find_color(colors, "blue")

    return red * green * blue

def main():
    file = open("input.txt", "r")
    data_list = file.read().split("\n")
    file.close()

    sum_powers = 0

    for item in data_list:
        power = get_power(item)
        sum_powers += power
    print (sum_powers)

    # power = get_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    # print(power)

if __name__ == "__main__":
    main()
