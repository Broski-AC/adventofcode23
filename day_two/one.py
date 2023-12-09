set_blocks = {
    "red": 12,
    "blue": 14,
    "green": 13
}

colors_key = {"red", "blue", "green"}

def game_validation(games):
    for game in games:
        colors_game = game.split(", ")
        
        instance_blocks = {}

        for game in colors_game:
            num, color = game.split()

            instance_blocks[color] = num


        for color in instance_blocks:
            value1 = int(set_blocks[color])
            value2 = int(instance_blocks[color])

            if value2 > value1:
                return False

    return True

def get_id(text):
    for s in text.split():
        if s.isdigit():
            return s

def parse_line(line):
    id_games = line.split(": ")
    id = get_id(id_games[0])

    games = id_games[1].split("; ")
    is_valid = game_validation(games)

    return int(id) if is_valid else 0
    
def main():
    file = open("input.txt", "r")
    data_list = file.read().split("\n")
    file.close()

    sum_ids = 0

    for item in data_list:
        id = parse_line(item)
        sum_ids += int(id)
    print (sum_ids)

if __name__ == "__main__":
    main()



