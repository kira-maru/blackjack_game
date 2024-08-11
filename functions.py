import random
CARDS = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5,
         "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
         "Jack": 10, "Queen": 10, "King": 10}


def deal_card_player(player_score):
    """Deals 2 cards. Returns score as INT and type of cards drawn as lists."""
    player_cards = []
    for deal in range(2):
        random_card_value = random.choice(list(CARDS.values()))
        player_cards.append(random_card_value)
        player_score += random_card_value

    return player_score, player_cards


def deal_card_computer(computer_score):
    """Deals 2 cards. Returns score as INT and type of cards drawn as lists."""
    computer_cards = []
    for deal in range(2):
        random_card_value = random.choice(list(CARDS.values()))
        computer_cards.append(random_card_value)
        computer_score += random_card_value

    return computer_score, computer_cards


def drawing_cards_player(p_score, p_cards):
    """Function returns accumulated score and ends
    in case the player gets over 21 points."""
    keep_drawing = True
    while keep_drawing:
        another_card = input("Do you want to draw a card? Write 'y' or 'n'\n")
        if another_card == 'y':
            random_card_value = random.choice(list(CARDS.values()))
            p_score += random_card_value
            if p_score == 21:
                print(f"You drew: {random_card_value}")
                return p_score, p_cards
            print(f"You drew: {random_card_value}")
            if p_score > 21 and 11 in p_cards:
                while p_score > 21 and 11 in p_cards:
                    ace_index = p_cards.index(11)
                    p_cards[ace_index] = 1
                    p_score -= 10
            else:
                return p_score, p_cards
        else:
            return p_score, p_cards

    return p_score, p_cards


def drawing_cards_pc(pc_score, pc_cards):
    """Function that calculates PC score. PC will keep drawing cards unless score is over 19 points.
    When over 21 points or 21 points, function ends and returns score."""
    keep_drawing_pc = True
    while keep_drawing_pc:
        if pc_score < 19:
            random_card_value = random.choice(list(CARDS.values()))
            pc_cards.append(random_card_value)
            pc_score += random_card_value

            if pc_score == 21:
                return pc_score, pc_cards
            elif pc_score > 21 and 11 in pc_cards:
                while pc_score > 21 and 11 in pc_cards:
                    ace_index = pc_cards.index(11)
                    pc_cards[ace_index] = 1
                    pc_score -= 10
            elif pc_score > 21:
                return pc_score, pc_cards
        else:
            return pc_score, pc_cards

    return pc_score, pc_cards


def final_results_message(player_result, pc_score, pc_cards):
    """Function that displays final results."""
    if player_result == 1:
        print(f"You WIN! PC scored {pc_score}. PC cards: {pc_cards}.")
    elif player_result == 0:
        print(f"It's a DRAW! PC scored {pc_score}. PC cards: {pc_cards}.")
    if player_result == -1:
        print(f"You LOSE! PC scored {pc_score}. PC cards: {pc_cards}.")


def last_calculation(score_player, score_pc, cards_pc):
    """Function that calculates all possible outcomes."""
    if score_player == 21 and score_pc != 21:
        final_results_message(1, score_pc, cards_pc)
    elif score_pc == 21 and score_player != 21:
        final_results_message(-1, score_pc, cards_pc)
    elif score_player == 21 and score_pc == 21:
        final_results_message(0, score_pc, cards_pc)
    elif score_pc > 21 and score_player <= 21:
        final_results_message(1, score_pc, cards_pc)
    elif score_player > 21 and score_pc <= 21:
        final_results_message(-1, score_pc, cards_pc)
    elif score_player > 21 and score_pc > 21:
        if score_player < score_pc:
            final_results_message(1, score_pc, cards_pc)
        elif score_player > score_pc:
            final_results_message(-1, score_pc, cards_pc)
        else:
            final_results_message(0, score_pc, cards_pc)
    elif score_player < 21 and score_pc < 21:
        if score_player > score_pc:
            final_results_message(1, score_pc, cards_pc)
        elif score_player < score_pc:
            final_results_message(-1, score_pc, cards_pc)
        else:
            final_results_message(0, score_pc, cards_pc)
    else:
        final_results_message(0, score_pc, cards_pc)



