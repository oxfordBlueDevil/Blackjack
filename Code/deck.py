import random

class Card(object):
    value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                  'K': 13, 'A': 14}

    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return "%s%s" % (self.number, self.suit)

    def __cmp__(self, other):
        return cmp(self.value_dict[self.number], self.value_dict[other.number])

class BlackjackCard(Card):
    def __init__(self, number, suit):
        super(BlackjackCard, self).__init__(number, suit)
        self.value_dict['J'] = 10
        self.value_dict['Q'] = 10
        self.value_dict['K'] = 10
        self.value_dict['A'] = 1

    def __add__(self, other):
        return self.value_dict[self.number] + self.value_dict[other.number]

    def __radd__(self, other):
        return self.value_dict[self.number] + other

    def get_card(self):
        return self.number

class Deck(object):
    def __init__(self):
        self.cards = []
        for num in Card.value_dict.keys():
            for suit in 'cdhs':
                self.cards.append(Card(num, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.isempty():
            return self.cards.pop()

    def add_cards(self, cards):
        self.cards.extend(cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return "%s%s" % (self.number, self.suit)

    def isempty(self):
        return self.cards == []

class BlackjackDeck(Deck):
    def __init__(self):
        self.cards = []
        for num in BlackjackCard.value_dict.keys():
            for suit in 'cdhs':
                self.cards.append(BlackjackCard(num, suit))

    def shuffle(self):
        self.__init__()
        super(BlackjackDeck, self).shuffle()
