class Player(object):
    def __init__(self):
        '''Creating the players hand.'''
        self.card = None                #initial card
        self.newcard = None             #newly drawn card
        self.ability = False            #only True if there is a shield on them

    def take(self, value):
        '''Function to represent first card in hand.'''
        self.card = value

    def ncard(self, value):
        '''Function to take second card in hand.'''
        self.newcard = value
