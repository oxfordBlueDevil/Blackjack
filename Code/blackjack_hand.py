class BlackjackHand(object):

    def __init__(self):
        self.cards = []

    def __cmp__(self, other):
        return cmp(self.hand_value(), other.hand_value())

    def __str__(self):
        s = ' '.join([str(c) for c in self.cards])
        return s

    def hand_value(self):
        total = sum(self.cards)
        if total < 12 and 'A' in [c.get_card() for c in self.cards]:
            total += 10
        return total

    def receive_card(self, c):
        self.cards.append(c)

    def reset_hand(self):
        self.cards = []
