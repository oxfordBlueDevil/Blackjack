from blackjack_hand import BlackjackHand

class BlackjackPlayer(object):
    def __init__(self, name, money = 100, is_dealer = False):
        self.name = name
        self.is_dealer = is_dealer
        self.hand = BlackjackHand()
        self.starting_balance = money
        self.wallet = money
        self.current_bet = 0
        self.won = False

    def hand_str(self, hide = False):
        s = str(self.hand)[3*hide:]
        if hide:
            return ''.join([self.name,' - Hand Cards ', s])
        else:
            return ''.join([self.name,' - Hand Cards ', s, ', Value = ', str(self.hand.hand_value())])

    def is_dealer(self):
        return self.is_dealer

    def get_wallet_balance(self):
        return self.wallet

    def bet(self, amount_bet):
        if type(amount_bet) != int:
            try:
                amount_bet = float(amount_bet)
            except:
                return
        if amount_bet > self.wallet:
            print 'You are betting (%s) more than your wallet balance (%s)' % (amount_bet, self.wallet)
            print 'We have set your bet to your wallet balance because you are not good enough for a line of credit.'
            self.current_bet += self.wallet
            self.wallet = 0
        else: 
            self.wallet -= amount_bet
            self.current_bet += amount_bet

    def calc_new_wallet_balance(self, payout_ratio):
        self.wallet += ( self.current_bet + self.current_bet * payout_ratio ) * self.won   # won when True is == 1, if False == 0
        self.current_bet = 0

