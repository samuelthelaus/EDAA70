import time

class MemoryGame:

    def __init__(self, board):
        self._board = board
        self.start_game()
        self._counter = 0

    def start_game(self):
        self._board.shuffle()

    def current_card_side_up(self, row, col):
        return self._board.get_card(row, col).current_side_up()

    def has_won(self):
        return self._board.has_won()

    def num_tries(self):
        return self._counter / 2

    def card_clicked(self, row, col):
        self._current_card = self._board.get_card(row, col)
        if not(self._current_card._front_up):
            self._counter += 1
            self._current_card.flip()
            if self._counter % 2 != 0:
                self._other_card = self._current_card
            else:
                return not(self._current_card.has_same_front(self._other_card))
                    
    def sleep_done(self):
        time.sleep(0.7)
        self._current_card.flip()
        self._other_card.flip()
