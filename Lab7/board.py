import numpy as np

class TicTacToeBoard:

    def __init__(self):
        self._board = np.full((3, 3), '-')

    def get(self, row, col):
        return self._board[row, col]

    def is_empty(self, row, col):
        return self.get(row, col) == '-'

    def place(self, marker, row, col):
        if self.is_empty(row, col) and marker in ['X', 'O']:
            self._board[row, col] = marker
            return True
        else:
            return False

    def is_full(self):
        return not (
            any(self._board[0,:] == '-') or
            any(self._board[1,:] == '-') or
            any(self._board[2,:] == '-')
        )

    def print_board(self):
        print(self._board)

    def is_winner(self, marker):
        if marker in ['X', 'O']:
            # Testa vågrätt och lodrätt
            for i in range(3):
                if all(self._board[i,:] == marker):
                    return True
                elif all(self._board[:,i] == marker):
                    return True
            
            # Testa diagonalerna
            if ((
                self._board[0, 0] == marker and
                self._board[1, 1] == marker and
                self._board[2, 2] == marker
                )
                or
                (
                    self._board[2, 0] == marker and
                    self._board[1, 1] == marker and
                    self._board[0, 2] == marker
                )):
                return True

        return False

