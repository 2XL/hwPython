# https://www.youtube.com/watch?v=1c4YPQTS35I

# CLI crazy eight game - auto shuffled -  play card with based on setting  -
"""
Get rid of the cards in your hand

"""


class Card(object):
    def __init__(self, rank, suite, wild_rank=8):
        self.rank = rank
        self.suit = suite
        self.point = self.set_points()
        self.wild_rank = wild_rank
        pass

    def compare_to(self, card):
        if card.rank == self.wild_rank:
            return self.compare_to_suite(card)
        elif self.rank == self.wild_rank:
            return True
        else:
            return self.rank == card.rank or self.suit == card.suite

    def is_place_holder(self, ):
        return self.rank == self.wild_rank
        pass

    def compare_to_suite(self, card):
        return self.suit == card.suite

    def set_points(self):
        if self.rank == self.wild_rank:
            return 50
        elif self.rank >= 10:
            return 10
        else:
            return self.rank

    def __str__(self):
        return self.rank + ' ' + self.suit


class Player(object):  # no more cards
    player_id = 0  # static class variable # no concurrency

    def __init__(self, name=None):
        self.name = "%s %d " % (name, Player.player_id)
        self.points = 0
        self.hand = {}
        self.round = 0
        self.strategy = 'fifo'
        self.card_stack = []
        self.card_wild = []  # substack of wildcard
        Player.player_id += 1
        pass

    def has_card(self, round_pointer):
        if len(self.card_wild + self.card_wild) is not 0:
            return True  # continue
        else:
            round_pointer.refresh_leaderboard()
            return False

        # player has more cards?
        # yes dealer ++ else round over
        pass

    def play(self, current_card=None):
        play_next = getattr(self, '_{}_play'.format(self.strategy))
        result = play_next(current_card)
        return result  # choose the next card to play from available
        pass

    def _fifo_play(self, current_card):
        # based on my hand play the card that best fits based on hand generation no order
        for card in self.hand.keys():  # get keys and filter by reg——xp keys that fits the current card
            if card.compare_to(current_card):
                self.hand.pop(card)
                return card
        return None
        pass

    def use_wild(self):
        return self.card_wild.pop()

    def add_card_to_stack(self, cards):
        self.card_stack += cards

    def tail_cards_continue_or_end(self):
        self.points += sum([v.points for k, v in self.hand])
        return self.points
        pass

    pass


class Game(object):  # no more deck
    def __init__(self, suit="XYZK", rank=13, table=2):
        self.rank = range(rank)
        self.suite = [_ for _ in suit]
        self.deck = [Card(rank=r, suite=suite) for (r, suite) in zip(self.rank, self.suite)]
        self.players = [Player() for _ in range(table)]
        self.dealer = 0
        self.play_order = 1
        self.current_set = []
        self.dealer_draw = 0
        self.draw_limit = 5
        pass

    def shuffle(self):
        pass

    def pick_player_ordr(self):
        pass

    def players_remaining_cards_tail(self):
        for player in self.players:
            player.tail_cards_continue_or_end()

        pass

    def draw_next_or_end(self):
        if self.deck is None:  # fin juego x quedar sin cartas
            return False
        card = self.deck.pop()

        if card.is_place_holder():
            self.deck.append(card)
            return True
            pass
        else:
            pass

        if self.players[self.dealer].play(card) and self.dealer_draw <= self.draw_limit:  # can play

            if self.players[self.dealer].has_card(self):  # if player no cards, end round due to no card
                return True
                pass

            self.dealer += self.play_order % len(self.players)  # next player
            self.dealer_draw = 0  # draw counter == 0
        else:
            self.dealer_draw += 1
            pass  # draw another card

    def refresh_leaderboard(self):
        end = False
        for player in self.players:
            if player.tail_cards_continue_or_end():
                end = True
        return end  # game ends

    def show_player_rank(self):
        # sort player by points
        return sorted(
            [(player.name, player.points) for player in self.players],
            key=lambda x: x[1]
        )


if "__name__" == "__main__":
    print("Crazy Game")

    game = Game()  # start the game
    game.shuffle()  # shuffle the cards
    game.pick_player_ordr()  # player pick random card to set the order
    while game.draw_next_or_end():
        continue
        pass
