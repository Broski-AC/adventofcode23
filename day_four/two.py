matches_dict = {}
card_stack = []

def matching(win, act):
    return sum(val in act for val in win)

def scrub(list):
    return [item for item in list if item.isdigit()]

def create_instance(num_matches, key):
    list = []
    start = int(key) + 1
    end = int(key) + num_matches + 1
    for inst in range(start, end):
        list.append(inst)

    matches_dict[key] = list

def count_cards(rows):
    total_cards = 0
    while len(card_stack) != 0:
        card = card_stack.pop()
        total_cards += 1

        if card in matches_dict:
            new_cards = matches_dict[card]

            for item in new_cards:
                if int(item) > rows:
                    next
                else:
                    card_stack.append(item)
        else:
            next
    
    return total_cards



def main():
    with open("small_input.txt") as file:
        rows = 0

        for line in file:
            rows += 1
            card_num, card = line.split(": ")
            key = card_num.split(" ")[1]
            winning_values, actual_values = card.split(" | ")
                       
            win_vals = scrub(winning_values.replace("\n", "").split(" "))
            act_vals = scrub(actual_values.replace("\n", "").split(" "))
            
            num_matches = matching(win_vals, act_vals)

            # Should get { 1: [2, 3, 4], 2: [3, 4], 3: [4, 5, 6, 7], etc...}
            create_instance(num_matches, key)
            card_stack.append(key)
        
        num_total_cards = count_cards(rows)
        print(num_total_cards)


    print(matches_dict)
    print(rows)

            


if __name__ == "__main__":
    main()