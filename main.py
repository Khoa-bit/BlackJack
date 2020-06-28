import random


class ACard:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def __repr__(self):
        return '<[ACard] Rank: {0!r}, Suit: {1!r}>'.format(self.rank, self.suit)


class DeckOfCards:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Space', 'Club', 'Diamond', 'Heart']
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = ACard(rank, suit)
                self.deck.append(card)

    def __repr__(self):
        return '<[DeckOfCards] deck: {0} cards>'.format(len(self.deck))

    def shuffle(self):
        random.shuffle(self.deck)


class Player:
    def __init__(self, n='Unknown'):
        self.name = n
        self.hand = []

    def __repr__(self):
        return '<[Player] name: {0}, hand: {1}>'.format(self.name, self.hand)

    def deal_hand(self, d):
        self.hand = d.deck[:2]
        d.deck = d.deck[2:]


"""Demo Section"""
# card0 = ACard('Three', 'Heart')
# print(card0)

deck0 = DeckOfCards()
deck0.shuffle()

players = [
    Player('One'),
    Player('Two'),
    Player('Three'),
    Player('Four'),
    Player('Five'),
    Player('Six'),
    Player('Seven')
]

player_num = 3
for nth in range(player_num):
    players[nth].deal_hand(deck0)
    print(len(deck0.deck))
    print(players[nth])




