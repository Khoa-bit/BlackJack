import random
import os


def clear():
    os.system('clear')


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
        # ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ranks = ['A', 'A', 'A']
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
        self.double = False
        self.summary = ''

    def __repr__(self):
        return '<[Player] name: {0!r}, {1!r}>' \
            .format(self.name, split_times)

    def player_turn(self, idx):
        global split_times
        show_table()
        self.display_info()

        # Five card Charlie
        if len(self.hand) == 5 and self.total[-1] <= 21:
            self.turn = False
            self.summary = 'Five card Charlie'
            print('==>FIVE CARD CHARLIE<==')
            input('(Any) End turn\n--> ')
        # Option
        elif self.total[-1] <= 21:
            self.check_double()
            if self.double and split_times < 3:
                print('(1) Hit | (2) End turn | (3) Split hand')
            else:
                print('(1) Hit | (2) End turn')
            option = input('--> ').upper()

            if option == '1':
                self.hit()
            elif option == '2':
                if self.ace and self.total[-2] <= 21:
                    self.summary = self.total[-2]
                else:
                    self.summary = self.total[-1]
                self.turn = False
            elif option == '3' and self.double and split_times < 3:
                # TODO: cannot split when a player has more than 2 cards
                split_times += 1
                self.split(idx)
        # Bust
        else:
            self.turn = False
            self.summary = 'Bust'
            print('==>Bust<==')
            input('(Any) End turn\n--> ')

    def display_info(self):
        global split_times
        # UI
        print('------{0}\'s turn------'.format(self.name))
        print(split_times)
        print('{0}\'s current Hand:'.format(self.name))
        for card in self.hand:
            print('- {0:>2} of {1}'.format(card.rank, card.suit))
        # Update and display the total
        self.update_ace()
        self.update_result()
        if self.ace and self.total[-2] <= 21:
            print('Total: {0} or {1}'.format(self.total[-1], self.total[-2]))
        else:
            print('Total: {0}'.format(self.total[-1]))

    def deal_hand(self, d):
        self.linked_deck = d
        # self.hand = self.linked_deck.deck[:2]
        self.hand = [ACard('A', 'Space'), ACard('A', 'Club')]
        self.linked_deck.deck = self.linked_deck.deck[2:]

        hand_ranks = [card.rank for card in self.hand]
        # Check and count Ace
        self.ace = hand_ranks.count('A')
        if self.ace and self.name != 'Dealer':
            for rank in ['10', 'J', 'Q', 'K']:
                if rank in hand_ranks:
                    # TODO: Dealers should reveal their cards lasts despite BlackJack
                    print('==>{0} gets BLACKJACK<=='.format(self.name))
                    self.summary = 'BlackJack'
                    self.turn = False

        self.check_double()

    def hit(self):
        self.double = False
        self.hand.append(self.linked_deck.deck[0])
        self.linked_deck.deck = self.linked_deck.deck[1:]

    def split(self, idx):
        global player_num
        global players
        global split_times
        self.double = False
        # Represent a new hand with a player with one copy of the double
        if split_times == 1:
            split_hand = Player(self.name + '(split)')
        else:
            split_hand = Player(self.name)
        split_hand.hand = [self.hand[0]]
        split_hand.linked_deck = self.linked_deck
        players.insert(idx + 1, split_hand)
        player_num += 1

        # Turn player into a split hand
        if split_times == 1:
            self.name = self.name + '(split)'
        self.hand.pop()

    def update_result(self):
        tmp_total = 0
        for card in self.hand:
            tmp_total += values[card.rank]

        self.total = [tmp_total - 10 * time for time in range(self.ace + 1)]

    def update_ace(self):
        hand_ranks = [card.rank for card in self.hand]
        self.ace = hand_ranks.count('A')

    def check_double(self):
        if len(self.hand) > 1:
            if self.hand[0].rank == self.hand[1].rank:
                self.double = True


def show_table():
    """Show all hands and the first card of the Dealer"""
    print('================Show Table================')
    for nth in range(player_num):
        if nth == 0:
            print('{0:>10}: '.format(players[nth].name), end='')
            tmp_str = '{0} of {1}'.format(players[nth].hand[0].rank, players[nth].hand[0].suit)
            print('{:<15}(***)'.format(tmp_str))
            continue

        print('{0:>10}: '.format(players[nth].name), end='')
        for card in players[nth].hand:
            tmp_str = '{0} of {1}'.format(card.rank, card.suit)
            print('{:<15}'.format(tmp_str), end='')
        print()
    print('==========================================')


class Dealer(Player):
    def __init__(self):
        super(Dealer, self).__init__('Dealer')


# Global variables
player_num = 0
while player_num < 2 or player_num > 8:
    player_num = int(input('Enter number of players (Max = 7): ')) + 1

split_times = 1

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
