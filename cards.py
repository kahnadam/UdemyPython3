class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        suits = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        values = ["Hearts","Diamonds","Clubs","Spades"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count],[num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

c = Card("4","Hearts")
d = Deck()
print(c)
print(d)
print(d._deal(3))
print(d.count())
