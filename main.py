from logic import clear, DeckOfCards, show_table, players, player_num


"""Demo Section"""
# card0 = ACard('Three', 'Heart')
# print(card0)

"""Black Jack"""
# Shuffle Deck
deck0 = DeckOfCards()
deck0.shuffle()

# Deal Player
for nth in range(player_num):
    players[nth].deal_hand(deck0)

clear()

# Table Turn
for nth in range(1, player_num):
    # Player turn
    while players[nth].turn:
        players[nth].player_turn()
        clear()

# Dealer Turn
while players[0].turn:
    players[0].player_turn()
    clear()

print('==========Summary==========')
for nth in range(player_num):
    print('{0:>13}: {1}'.format(players[nth].name, players[nth].summary))
