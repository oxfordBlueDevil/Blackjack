from blackjack_player import BlackjackPlayer
from deck import BlackjackDeck

class Blackjack(object):
    def __init__(self, human = True):
        self.human = human
        self.game_deck = BlackjackDeck()
        self.game_deck.shuffle()
        self.dealer = self.create_dealer('Dealer')
        self.game_counter = 0

        self.PAYOUT = 1.5
        self.DEALER_THRESHOLD = 17
        self.ANTE = 5

    def create_player(self, title):
        if self.human:
            name = raw_input("Enter %s's name: " % title)
        else:
            name = title
        return BlackjackPlayer(name)

    def create_dealer(self, title):
        if self.human:
            name = raw_input("Enter %s's name: " % title)
        else:
            name = title
        return BlackjackPlayer(name, money = 0, is_dealer = True)

    def deal_cards(self,n = 2):
        for _ in xrange(n):
            for player in self.players:
                player.hand.receive_card(self.game_deck.draw_card())
            self.dealer.hand.receive_card(self.game_deck.draw_card())
        for player in self.players:
            print player.hand_str()
        print self.dealer.hand_str(True)

    def actionHit(self, player, action = ''):
        if self.human:
            if action == 'H':
                return True
            elif action == 'S':
                return False
            else:
                player.bet(raw_input("%s Make a bet: $" %player.name))
                player_action = raw_input("%s Hit or Stand? (H/S): " %player.name).upper()
                return self.actionHit(player, player_action)
        else:
            if player.hand.hand_value() > 19:
                player.bet(10)
            elif player.hand.hand_value() < 12 and player.hand.hand_value() > 8:
                player.bet(5)
            return player.hand.hand_value() < self.DEALER_THRESHOLD

    def announce_winners(self, player):
        player.calc_new_wallet_balance(self.PAYOUT)
        print '%s Wallet Balance - $' %player.name  + str(player.wallet)
        if player.won:
            print '%s Congratulations!  You have won this round.' %player.name
        else:
            print 'Dealer won :('
            print 'Sorry... try again?'

    def play_next_round(self):
        all_busted = []
        for player in self.players:
            # Handle all player hits
            while player.hand.hand_value() < 22 and self.actionHit(player):
                player.hand.receive_card(self.game_deck.draw_card())
                print player.hand_str()
                print self.dealer.hand_str(True)

            # did player bust
            if player.hand.hand_value() > 21:
                print 'Player busted...'
                print player.hand_str()
                self.announce_winners(player)
                all_busted.append(True)
            else:
                all_busted.append(False)
            # great score
            if player.hand.hand_value() == 21:
                print 'Congratulations!  You have Blackjack!!!'
                player.won = True
                self.announce_winners(player)

        if all(all_busted):
            return

        while self.dealer.hand.hand_value() < self.DEALER_THRESHOLD:
            self.dealer.hand.receive_card(self.game_deck.draw_card())

        if self.dealer.hand.hand_value() > 21:
            print 'Dealer busted...'
            print self.dealer.hand_str()

        for player in self.players:
            print player.hand_str()
            if player.hand.hand_value() < 21:
                player.won = player.hand >= self.dealer.hand or self.dealer.hand.hand_value() > 21
                self.announce_winners(player)

        print self.dealer.hand_str()

    def howManyPlayers(self):
        if self.human:
            nPlayers = int(raw_input("Enter the number of players (no more than 10):"))
            self.players = [self.create_player('Player %s' %str(i+1)) for i in xrange(nPlayers)] 

    def playAgain(self, action = ''):
        if self.human:
            if action == 'Y':
                return True
            elif action == 'N':
                return False
            else:
                player_action = raw_input("Do you want to play another round (Y/N): ").upper()
                return self.playAgain(player_action)
        else:
            return self.game_counter < 100

    def play_game(self):
        self.howManyPlayers()
        while True:
            for player in self.players:
                player.hand.reset_hand()
                player.won = False
                player.bet(self.ANTE)

            self.dealer.hand.reset_hand()
            self.game_deck.shuffle()
            self.deal_cards()
            self.play_next_round()
            self.game_counter += 1
            if not self.playAgain():
                break

        # if self.player.wallet < 5:
        #     print "Sorry... You suck at this game."


if __name__ == '__main__':
    game = Blackjack()
    game.play_game()
