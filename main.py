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
        self.turn = True
        self.result = 0
        self.linked_deck = None

    def __repr__(self):
        return '<[Player] name: {0}, turn: {2}, result: {3}, hand: {1}, linked deck: {4}>'\
            .format(self.name, self.hand, self.turn, self.result, self.linked_deck)

    def player_turn(self):
        print('------{0}\'s turn------'.format(self.name))
        print('{0}\'s current Hand:'.format(self.name))
        for card in self.hand:
            print('- {0:>2} of {1}'.format(card.rank, card.suit))
        print('(1) Hit | (2) End turn')
        option = input('--> ')

        if option == '1':
            self.hit()
        elif option == '2':
            self.turn = False

    def deal_hand(self, d):
        self.linked_deck = d
        self.hand = self.linked_deck.deck[:2]
        self.linked_deck.deck = self.linked_deck.deck[2:]

    def hit(self):
        self.hand.append(self.linked_deck.deck[0])
        self.linked_deck.deck = self.linked_deck.deck[1:]

    def split(self, d):
        pass

    def update_result(self):
        pass


"""Demo Section"""
# card0 = ACard('Three', 'Heart')
# print(card0)

deck0 = DeckOfCards()
deck0.shuffle()

players = [
    Player('Dealer'),
    Player('One'),
    Player('Two'),
    Player('Three'),
    Player('Four'),
    Player('Five'),
    Player('Six'),
    Player('Seven')
]

player_num = 4
for nth in range(player_num):
    players[nth].deal_hand(deck0)
    # print(len(deck0.deck))
    # print(players[nth])

# Table Turn
for nth in range(1, player_num):
    # Table turn
    while players[nth].turn:
        players[nth].player_turn()
        # players[nth].turn = int(input("{0} End turn: ".format(players[nth].name)))
        pass



