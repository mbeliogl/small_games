import random

class Card:
    def __init__(self, value, suit):
    
        if value > 13 or value < 1:
            return None
        if suit not in 'HDSC':
            return None

        self.value = value
        self.suit = suit

    def getValue(self):
        return self.value
        
    def getSuit(self):
        return self.suit
        
    def setValue(self, newValue):
        if newValue > 13 or newValue < 1:
            return None
        else:
            self.value = newValue
    
    def setSuit(self, newSuit):
        if newSuit not in 'HDSC':
            return None
        else:
            self.suit = newSuit

    def __eq__(self, otherCard):
        return self.getValue() == otherCard.getValue()
        
    def __lt__(self, otherCard):
        return self.getValue() < otherCard.getValue()
    
    def __le__(self, otherCard):
        return self.getValue() <= otherCard.getValue()
    
    def __gt__(self, otherCard):
        return self.getValue() > otherCard.getValue()

    def __ge__(self, otherCard):
        return self.getValue() >= otherCard.getValue()

    def __ne__(self, otherCard):
        return self.getValue() != otherCard.getValue()

    def __str__(self):
        c = str(self.value) + str(self.suit)
        return c

class Deck:
    def __init__(self):
        
        self.Deck = []
        for suit in ['S', 'D', 'H', 'C']:
            for i in range(1,14):
                self.Deck.append(Card(i, suit))

    def printDeck(self):
        for card in self.Deck:
            print(card)
        
    def shuffle(self):
        random.shuffle(self.Deck)
   
    def cut(self):
        index = random.randint(0, len(self.Deck))
        self.Deck = self.Deck[index:] + self.Deck[:index]

    def takeTop(self):
        topCard = self.Deck.pop()
        return topCard

    def __len__(self):
        length = len(self.Deck)
        return length

    