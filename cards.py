class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Card:
    allowed_value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    allowed_suit = ["Hearts","Diamonds","Clubs","Spades"]

    def __init__(self,suit,value):
        if suit not in Card.allowed_suit:
            raise ValueError(f"You can't have {suit} as a suit")
        if value not in Card.allowed_value:
            raise ValueError(f"You can't have {value} as a value")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    cards_in_deck = 0

    def __init__(self):
        cards = []
        allowed_value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        allowed_suit = ["Hearts","Diamonds","Clubs","Spades"]
        i = 0
        while i < 4:
            for v in allowed_value:
                cards.append(str(v + " of " + allowed_suit[i]))
            i += 1
        Deck.cards_in_deck = len(cards)

    def __repr__(self):
        return f"Deck of {self.cards_in_deck} cards"


my_deck = Deck()
print(my_deck)
