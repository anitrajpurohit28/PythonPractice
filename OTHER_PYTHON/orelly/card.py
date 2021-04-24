# card.py
"""Card class that represent a playing card and ita image file name."""

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """Initialize a card with face and suit."""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the card's self._suit value."""

    @property
    def image_name(self):
        """Return the card's image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation of repr()."""
        return f"Card(face='{self._face}', suit='{self._suit}')"

    def __str__(self):
        """Return the string representation of str()."""
        return f'{self._face} of {self._suit}'

    def __format__(self, format):
        """Returns the formatted string representation"""
        return f'{str(self):{format}}'
