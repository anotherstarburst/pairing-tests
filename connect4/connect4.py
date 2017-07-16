import os


class Game(object):
    def __init__(self, x_length=7, y_length=6, winning_length=4):
        self.board = []
        self.players = []
        self.x_length = x_length
        self.y_length = y_length
        self.winning_length = winning_length

    def _print_board(self):
        os.system('clear')
        print "  ",
        print "  ".join(map(str, range(len(self.board[0]))))
        for rw_nr, rw in enumerate(self.board):
            print rw_nr,
            for col in rw:
                print " " + col,
            print '\n'

    def _player_symbol(self, player):
        sym = 'x' if player == self.players[0] else 'o'
        return sym

    def _get_position(self, player):
        valid = False
        while not valid:
            pos = str(raw_input(player.title() +
                                " please enter your next position (y, x) "))
            pos = pos.split(',')
            valid, pos = self._validate(pos)
        return pos

    def _validate(self, position):
        if not position:
            print "please enter a position in the form (y,x)"
            return False, position

        if len(position) != 2:
            print "please enter a position in the form (y,x)"
            return False, position

        try:
            position = map(int, position)
        except:
            print "please enter a position in the form (y,x) and ensure they are integers"
            return False, position

        if position[0] < 0 or position[1] < 0:
            print "invalid position"
            return False, position

        if (position[0] > self.y_length - 1) or (position[1] > self.x_length-1):
            print "invalid position"
            return False, position

        if self.board[position[0]][position[1]] != '.':
            print "attempting to overwrite existing move"
            return False, position

        return True, position

    def _place_piece(self, pos, player):
        sym = self._player_symbol(player)
        self.board[pos[0]][pos[1]] = sym

    def _check_for_winning_line(self, player):
        sym = self._player_symbol(player)
        if self._check_horizontal(sym):
            return True
        elif self._check_vertical(sym):
            return True
        elif self._check_diag_left(sym):
            return True
        elif self._check_diag_right(sym):
            return True
        return False

    def _check_horizontal(self, sym):
        for rw in self.board:
            count = 0
            for col in rw:
                if col == sym:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        return False

    def _check_vertical(self, sym):
        for col_nr in range(len(self.board[0])):
            count = 0
            for row in self.board:
                if row[col_nr] == sym:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        return False

    def _check_diag_right(self, sym):
        for row_nr, row in enumerate(self.board):
            count = 0
            for col_nr, col in enumerate(row):
                if col == sym:
                    count += 1
                    while count > 0:
                        if row_nr+count >= self.y_length or col_nr+count >= self.x_length:
                            count = 0
                            break
                        if self.board[row_nr+count][col_nr+count] == sym:
                            count += 1
                        else:
                            count = 0
                        if count == 4:
                            return True

        return False

    def _check_diag_left(self, sym):
        for row_nr, row in enumerate(self.board):
            count = 0
            for col_nr, col in enumerate(row):
                if col == sym:
                    count += 1
                    while count > 0:
                        if row_nr+count >= self.y_length or col_nr-count < 0:
                            count = 0
                            break
                        if self.board[row_nr+count][col_nr-count] == sym:
                            count += 1
                        else:
                            count = 0
                        if count == 4:
                            return True
        return False

    def test(self):
        blank_row = ['x' for cnt in range(self.x_length)]
        self.board = [list(blank_row) for col in range(self.y_length)]
        self.players = ["test x", "test o"]
        self._print_board()
        print self._check_diag_left('x')

    def create_board(self):
        blank_row = ['.' for cnt in range(self.x_length)]
        self.board = [list(blank_row) for col in range(self.y_length)]

    def add_player(self, name):
        if not name:
            print "Please enter a name"
            return False
        if name in self.players:
            print "Error - player already present"
            return False

        self.players.append(name)
        return True

    def play(self):
        while True:
            for player in self.players:
                self._print_board()
                pos = self._get_position(player)
                self._place_piece(pos, player)
                if self._check_for_winning_line(player):
                    self._print_board()
                    print player + " has won the game!! "
                    exit(0)


def init():
    game = Game()
    # game.test()
    game.create_board()
    for pl in range(1, 3, 1):
        while True:
            pl_name = str(raw_input("Please enter the name of player " + str(pl) + ": "))
            if game.add_player(pl_name):
                break

    return game


def main():
    game = init()
    game.play()
    exit(0)

if __name__ == "__main__":
    main()