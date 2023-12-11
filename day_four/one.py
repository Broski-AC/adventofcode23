def matching(win, act):
    return sum(val in act for val in win)

def scrub(list):
    return [item for item in list if item.isdigit()]

def main():
    points = 0

    with open("input.txt") as file:
        for line in file:
            card = line.split(": ")[1]
            winning_values, actual_values = card.split(" | ")

            win_vals = scrub(winning_values.replace("\n", "").split(" "))
            act_vals = scrub(actual_values.replace("\n", "").split(" "))
            
            num_matches = matching(win_vals, act_vals)

            if num_matches == 0:
                next
            else:
                current_points = 1 * pow(2, num_matches - 1)
                points += current_points
            
        print(points)


if __name__ == "__main__":
    main()