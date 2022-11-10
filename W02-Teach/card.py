from random import randrange

class Card():
    """
    Card class holds value.
    """

    def card_number(self):
        """
        value of the card is ranged from 1 to 13
        """
        return (randrange(1,13))