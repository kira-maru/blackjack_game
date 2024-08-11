import sys
from functions import (deal_card_player, deal_card_computer, drawing_cards_player, drawing_cards_pc,
                       last_calculation)


SCORE_PLAYER = 0
SCORE_COMPUTER = 0

game_on = True

while game_on:
    start_game = input("Welcome to the Blackjack game! Write 'start' to start the game!\n")
    if start_game != "start":
        sys.exit()
    player_hand = deal_card_player(SCORE_PLAYER)
    computer_hand = deal_card_computer(SCORE_COMPUTER)

    print(f"Your cards are: {player_hand[1]}. One of computer's card is: {computer_hand[1][0]}.")

    final_score_player = drawing_cards_player(*player_hand)
    final_score_pc = drawing_cards_pc(*computer_hand)

    print(f"Your final score is: {final_score_player[0]}. Your cards: {final_score_player[1]}.")

    last_calculation(final_score_player[0], final_score_pc[0], final_score_pc[1])
    break



