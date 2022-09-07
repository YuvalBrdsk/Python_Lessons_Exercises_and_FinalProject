"""Class which has a description of every card in the game"""
class Card:
    """Every card has two properties: a value and a suit"""
    def __init__(self,value,suit):
        self.card_value = value
        self.card_suit = suit

    def __repr__(self):
        """Function which allows to print card's properties"""
        return f"The card's value is {self.value_name()} of {self.suit_name()}"


    def __gt__(self, other):
        """Function which checks cards' values in order to find the grater one"""
        if self.card_value>other.card_value:
            return True
        else:
            return False

    def __eq__(self, other):
        """Function which compares cards' values in order to determine whether they are equal"""
        if self.card_value == other.card_value:
            return True
        else:
            return False

    def suit_name(self):
        """Functions which returns a suit name of every card's value"""
        if self.card_suit == 1:
            return f"Diamond"
        elif self.card_suit == 2:
            return f"Spade"
        elif self.card_suit == 3:
            return f"Heart"
        elif self.card_suit == 4:
            return f"Club"

    def value_name(self):
        """Function which returns special value names (Ace, Jack, Queen, King)"""
        if self.card_value == 1:
            return f"Ace"
        elif self.card_value == 11:
            return f"Jack"
        elif self.card_value == 12:
            return f"Queen"
        elif self.card_value == 13:
            return f"King"
        else:
            return str(self.card_value)

