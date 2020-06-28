class ACard:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def __repr__(self):
        return '<Rank: {0!r}, Suit: {1!r}>'.format(self.rank, self.suit)


card0 = ACard('Three', 'Heart')
print(card0)