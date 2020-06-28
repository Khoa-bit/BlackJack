import random

# Global Variables
values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}


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
        return '<[DeckOfCards] deck: {0!r} cards>'.format(len(self.deck))

    def shuffle(self):
        random.shuffle(self.deck)


class Player:
    def __init__(self, n='Unknown'):
        self.name = n
        self.hand = []
        self.turn = True
        self.total = []
        self.linked_deck = None
        self.ace = 0

    def __repr__(self):
        return '<[Player] name: {0!r}, turn: {2!r}, total: {3!r},ace: {5!r}, hand: {1!r}, linked deck: {4!r}>'\
            .format(self.name, self.hand, self.turn, self.total, self.linked_deck, self.ace)

    def player_turn(self):
        # UI
        print('------{0}\'s turn------'.format(self.name))
        print('{0}\'s current Hand:'.format(self.name))
        for card in self.hand:
            print('- {0:>2} of {1}'.format(card.rank, card.suit))
        if self.ace and self.total[-2] <= 21:
            print('Total: {0} or {1}'.format(self.total[-1], self.total[-2]))
        else:
            print('Total: {0}'.format(self.total[-1]))

        # Five card Charlie
        if len(self.hand) == 5 and self.total[-1] <= 21:
            self.turn = False
            print('==>FIVE CARD CHARLIE<==')
            input('(Any) End turn\n--> ')
        # Option
        elif self.total[-1] <= 21:
            print('(1) Hit | (2) End turn')
            option = input('--> ')

            if option == '1':
                self.hit()
            elif option == '2':
                self.turn = False
        # Bust
        else:
            self.turn = False
            print('==>Bust<==')
            input('(Any) End turn\n--> ')

    def deal_hand(self, d):
        self.linked_deck = d
        # self.hand = self.linked_deck.deck[:2]
        self.hand = [ACard('9', 'Club'), ACard('10', 'Space'), ACard('A', 'Space'), ACard('A', 'Space')]
        self.linked_deck.deck = self.linked_deck.deck[2:]

        hand_ranks = [card.rank for card in self.hand]
        self.ace = hand_ranks.count('A')
        if self.ace and ['10', 'J', 'Q', 'K'] in hand_ranks:
            print('=={0} gets BlackJack=='.format(self.name))
            self.turn = False

        self.update_result()

    def hit(self):
        self.hand.append(self.linked_deck.deck[0])
        self.linked_deck.deck = self.linked_deck.deck[1:]
        self.update_result()

    def split(self, d):
        pass

    def update_result(self):
        tmp_total = 0
        for card in self.hand:
            tmp_total += values[card.rank]

        self.total = [tmp_total - 10 * time for time in range(self.ace + 1)]


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
