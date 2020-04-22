class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __add__(self, other):
        return self.rank + other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if value not in range(14):
            raise ValueError
        self._rank = value
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value not in range(4):
            raise ValueError
        self._suit = value
