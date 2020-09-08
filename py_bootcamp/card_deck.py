from random import shuffle
class Card:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '{} of {}'.format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for suit in Card.suits for value in Card.values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return 'Deck of {} cards'.format(self.count())

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError('No more cards left')

        popped_cards = []
        for i in range(num):
            if self.count() != 0:
                popped_cards.append(self.cards.pop())

        return popped_cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')

        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)


