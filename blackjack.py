from random import choice


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calc_score(cards):
    # Check if player already has blackjack with first 2 cards:
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Turn 11 card to 1 if sum is over 21:
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


computer_cards = []
user_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Game loop
while not is_game_over:
    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)

    print(f'Your cards: {user_cards}, current score: {user_score}')
    print(f'Computer\'s first card: {computer_cards[0]}')

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        another_card = input('Type "y" to get another card, "n" to pass ')
        if another_card == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
