import random


class Game(object):
    """
    Note, if required to win is passed it can not be greater than
    (finish - start + 1) / 2
    """
    def __init__(self, start=1, finish=10, deck_count=1, required_to_win=5):
        self.start = start
        self.finish = finish
        self.deck_count = deck_count
        self.card_count = (finish-start+1) * deck_count
        self.required_to_win = required_to_win
        self.correct_guesses = 0
        self.deck = []
        if required_to_win > ((finish - start + 1) / 2):
            print """
            You've asked for impossible winning criteria...
            Please ensure that (finish - start + 1) / 2 is 
            greater than or equal to required_to_win
            """
            self._check_replay()



    def _fill_deck(self):
        self.deck = [crd for crd in range(self.start, self.finish + 1, 1)]
        self.deck = self.deck * self.deck_count
        return

    def _shuffle_deck(self):
        random.shuffle(self.deck)
        return

    def _draw_card(self):
        return self.deck.pop()

    def _check_guess(self, card, guess):
        new_card = self._draw_card()
        valid_guesses = ['l', 'lower', 'higher', 'h']
        if not guess or guess not in valid_guesses:
            print "Oops... your keyboard skills are failing you... loose a point!"
            self.correct_guesses -= 1
            return False

        if guess == "l" or guess == "lower":
            if new_card > card:
                print "New Card: " + str(new_card) + " > " + str(card)
                print "Oops... your psychic powers are failing you... that was incorrect."
                return False

        if guess == "h" or guess == "higher":
            if new_card < card:
                print "New Card: " + str(new_card) + " < " + str(card)
                print "Oops... your psychic powers are failing you... that was incorrect."
                return False
        print "Correct! New Card: " + str(new_card)
        self.correct_guesses += 1
        return True

    def _print_score(self):
        print "Score: " + str(self.correct_guesses) + " / " + str((self.card_count - len(self.deck))/2)

    def _check_win(self):
        max_correct = (self.card_count - len(self.deck)) / 2
        if self.correct_guesses >= self.required_to_win:
            print "You have won the game!"
            return True

        print "You have lost the game!"
        return False

    def _check_replay(self):
        play_again = str(raw_input("Do you want to play again (y / n)? ")).strip().lower()
        if play_again == "n":
            return False
        return True

    def _end_of_game(self):
        self._check_win()
        if not self._check_replay():
            print "Thanks for playing!"
            exit(0)
        else:
            self.setup()

    def setup(self):
        """
        Fills the deck with the number of cards required
        Shuffles the deck
        Resets the correct number of guesses.
        """
        self._fill_deck()
        self._shuffle_deck()
        self.correct_guesses = 0
        return

    def play(self):
        """
        Begins game play.
        """

        while True:
            self._print_score()
            card = self._draw_card()
            guess = str(raw_input("Is the next card going to be higher (h) or lower (l) than " + str(card) + "? ")).strip().lower()
            correct = self._check_guess(card, guess)

            if self.required_to_win >= (self.correct_guesses + (len(self.deck) / 2)):
                # not enough cards left to win the game
                self._end_of_game()

            if len(self.deck) <= 0:
                # no cards left in deck
                self._end_of_game()


def main():
    game = Game()
    game.setup()
    game.play()
    exit(0)

if __name__ == "__main__":
    main()
