from logic import clear, DeckOfCards
import logic


"""Demo Section"""
# card0 = ACard('Three', 'Heart')
# print(card0)

"""Black Jack"""
# Shuffle Deck
deck0 = DeckOfCards()
deck0.shuffle()

# Deal Player
for nth in range(logic.player_num):
    logic.players[nth].deal_hand(deck0)

clear()

# Table Turn
nth = 1
while nth < logic.player_num:
    # Player turn
    while logic.players[nth].turn:
        logic.players[nth].player_turn(nth)
        clear()
    nth += 1
    logic.split_times = 0

# Dealer Turn
while logic.players[0].turn:
    logic.players[0].player_turn(0)
    clear()

print('==========Summary==========')
for nth in range(logic.player_num):
    print('{0:>13}: {1}'.format(logic.players[nth].name, logic.players[nth].summary))
