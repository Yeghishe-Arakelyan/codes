import random


def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    random.shuffle(deck)

    return deck


def get_card_value(card):
    rank = card.split()[0]

    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11
    else:
        return int(rank)
    

def game():
    player1_score = 0
    player2_score = 0
    player1_hand = []
    player2_hand = []
    deck = create_deck()
    print('Welcome to the game!')

    while player1_score < 10 and player2_score < 10:

        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())

        p1 = get_card_value(player1_hand[-1])
        p2 = get_card_value(player2_hand[-1])

        if p1 > p2:
            print(f'{player1_hand[-1]}, {player2_hand[-1]} player 1 win!')
            player1_score += 1

        elif p2 > p1:
            print(f'{player1_hand[-1]}, {player2_hand[-1]} player 2 win!')
            player2_score += 1

        else:
            print(f'{player1_hand[-1]}, {player2_hand[-1]} tie!')

        if player1_score == 10 or player2_score == 10:

            if player1_score > player2_score:
                print(f'Game over!\nPlayer 1 wins {player1_score}-{player2_score}.')

            elif player2_score > player1_score:
                print(f'Game over!\nPlayer 2 wins {player1_score}-{player2_score}.')    

game()

