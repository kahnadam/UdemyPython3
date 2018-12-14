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
