import random

class Deck(object):
    def __init__(self):
        self.cards = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
            ] * 4

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def draw(self):
        return self.cards.pop()


class Player(object):
    def __init__(self):
        self.hand = []
        self.name = ""

    def add_card(self, deck):
        self.hand.append(deck.draw())

    def hand_value(self):
        card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }
        value = 0
        for card in self.hand:
            value += card_values[card]
        return value



def start_game(players):
    deck = Deck()
    deck.shuffle()
    player_dict = {}
    for player_name in players:
        player = Player()
        player.name = player_name
        player.add_card(deck)
        player.add_card(deck)
        player_dict[player_name] = player

    return player_dict, deck


def main():
    print ("======================\nLets play a game of 21 \n======================")
    players, deck = start_game(["Sam", "Dealer"])
    while True:
        for pl_name in players.keys():
            player = players[pl_name]
            print player.name + ": " + str(player.hand_value())

            if player.hand_value() == 21:
                print player.name + " has won the game! with a hand of: " + str(player.hand)
                exit(0)

            if player.hand_value() > 21:
                print player.name + " has lost the game! with a hand of: " + str(player.hand)
                exit(0)

            if player.name != "Dealer":
                if player.hand_value() < 17:
                    player.add_card(deck)
            
            if player.name == "Dealer" and players["Sam"].hand_value() >= 17:
                if players["Dealer"].hand_value() > players["Sam"].hand_value():
                    print player.name + " has won the game! with a hand of: " + str(player.hand)
                    exit(0)
                else:
                    player.add_card(deck)
        _ = raw_input("Press any key to continue \n")



if __name__ == "__main__":
    main()
    exit(0)