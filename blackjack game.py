import random
import sys


#dictionary for cards and cards' values
cards = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5,
           "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10}


score_player = 0
score_computer = 0 
    

def first_deal(score_player, score_computer):
    """Function that deals 2 cards for player and PC; returns score and type of cards drawn as lists."""
    cards_player = []
    cards_computer = []
    for deal in range(2):
        random_card_value = random.choice(list(cards.values()))
        cards_player.append(random_card_value)
        score_player+=random_card_value

        random_card_value = random.choice(list(cards.values()))
        cards_computer.append(random_card_value)
        score_computer+=random_card_value

    list_score = [score_player, score_computer]
    list_cards = [cards_player, cards_computer]

    return list_score, list_cards


def drawing_cards_player(calculate_first):
    """Function that takes returned score and list of cards from calculate_first function in order
    to let the player draw cards or pass. Function will return accumulated score and will end 
    in case the player gets over 21 points."""
    keep_drawing = True
    while keep_drawing:
        another_card = input("Do you want to draw a card? Write 'y' or 'n'\n")
        if another_card == 'y':
            random_card_value = random.choice(list(cards.values()))
            calculate_first[0][0]+=random_card_value
            if calculate_first[0][0] == 21:
                print(f"You drew: {random_card_value}")
                return calculate_first[0][0]
            print(f"You drew: {random_card_value}")
            if calculate_first[0][0] > 21:
                if 11 in calculate_first[1][0]:
                    ace_index = calculate_first[1][0].index(11) 
                    calculate_first[1][0][ace_index] = 1
                    calculate_first[0][0] -= 10 
                else:
                    keep_drawing = False
                    return calculate_first[0][0]
        elif another_card == 'n':
            keep_drawing = False

    return calculate_first[0][0]

        
def drawing_cards_pc(calculate_first):
    """Function that calculates PC score. PC will keep drawing cards unless it's over 19 points.
    When over 21 points or 21 points, function will end and return score."""
    keep_drawing_pc = True
    while keep_drawing_pc:
        if calculate_first[0][1] <= 19:
            random_card_value_pc = random.choice(list(cards.values()))
            calculate_first[0][1]+=random_card_value_pc
            if calculate_first[0][1] == 21:
                return calculate_first[0][1]
            if calculate_first[0][1] > 21:
                if 11 in calculate_first[1][1]:
                    ace_index = calculate_first[1][1].index(11)
                    calculate_first[1][1][ace_index] = 1
                    calculate_first[0][1] -= 10
            else:
                keep_drawing_pc = False
                return calculate_first[0][1]
        else:
            keep_drawing_pc = False
     
    return calculate_first[0][1]

def final_results_message(pc_score, player_win):
    """Function that displays final results."""
    if player_win == 1:
        print(f"You WIN! PC scored {pc_score}.")
    elif player_win == 0:
        print(f"It's a DRAW! PC scored {pc_score}.")
    if player_win == -1:
        print(f"You LOSE! PC scored {pc_score}.")


def last_calculation(final_score_player, final_score_pc):
    """Function that calculates who wins - player or PC."""
    if final_score_player > 21:
        final_results_message(final_score_pc, -1)
    elif final_score_pc > 21:
        final_results_message(final_score_pc, 1)
    elif final_score_player > final_score_pc:
        final_results_message(final_score_pc, 1)
    elif final_score_player < final_score_pc:
        final_results_message(final_score_pc, -1)
    else:
        final_results_message(final_score_pc, 0)

    

starting = input("Welcome to the Blackjack game! Write 'start' to start the game!\n")
if starting != 'start':
    sys.exit(0)
calculate_first = first_deal(score_player, score_computer)

print(f"Your cards are: {calculate_first[1][0]}. One of computer's card is: {calculate_first[1][1][1]}.")

final_score_player = drawing_cards_player(calculate_first)
final_score_pc = drawing_cards_pc(calculate_first)

print(f"Your final score is: {final_score_player}")
last_calculation(final_score_player, final_score_pc)





    
    
            










