class deck(object):
    '''Deck of cards'''
    class node(object):
        '''Stores each card'''
        def __init__(self, card, link):
            self.value = card
            self.link = link
    def __init__(self):
        self.head = None
    def push(self, value):
        self.head = deck.node(value, self.head)
    def draw(self):
        try:
            value = self.head.value
            self.head = self.head.link
        #When the deck of cards is finished, self.head needs a value, if not there will be an AtrributeError
        except AttributeError: 
            value = None
            self.head = None
        return value
