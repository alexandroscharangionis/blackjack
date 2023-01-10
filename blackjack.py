from random import choice


def deal_card(card_stack):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    card_stack.append(card)


def calc_score(card_stack):
    score = 0
    for card in card_stack:
        if card + score > 21 and card == 11:
            card = 1
            print("card was 11, but has been converted to 1")
        score += card
    return score


def check_for_winner(player_score, computer_score):
    if player_score == 21 or computer_score == 21:
        print(f'{"Player" if player_score == 21 else "Computer"} wins')


computer_stack = []
player_stack = []
computer_score = 0
player_score = 0

start_game = input('Want to play a game of blackjack? "y" or "n" ')
if start_game == 'y':
    for _ in range(2):
        deal_card(computer_stack)
        deal_card(player_stack)
    # while True:
    computer_score = calc_score(computer_stack)
    player_score = calc_score(player_stack)
    check_for_winner(player_score, computer_score)
    print(computer_score)
    print(player_score)
    print(computer_stack)
    print(player_stack)
