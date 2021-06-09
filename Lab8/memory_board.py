import numpy as np
import random

class MemoryCard:
    def __init__(self, front_filename, back_filename):
        self._front_filename = front_filename
        self._back_filename = back_filename
        self._front_up = False

    def current_side_up(self):
        if self._front_up:
            return self._front_filename
        else:
            return self._back_filename

    def is_front_up(self):
        return self._front_up

    def has_same_front(self, other_card):
        return self._front_filename == other_card._front_filename

    def flip(self):
        self._front_up = not(self._front_up)

    def __str__(self):
        return f'C({self._front_up}, {self._front_filename}, {self._back_filename})'

    def __repr__(self):
        return str(self)


class MemoryBoard:
    def __init__(self, size, front_filenames, back_filename):
        self._size = int(size)
        self._front_filenames = random.sample(front_filenames, self._size*self._size//2)
        self._back_filename = back_filename

    def shuffle(self):
        self._card_list = [MemoryCard(item, self._back_filename) for item in self._front_filenames for _ in range(2)]
        random.shuffle(self._card_list)
        self._card_array = np.reshape(np.array(self._card_list), (self._size, self._size))

    def get_card(self, row, col):
        return self._card_array[row, col]

    def size(self):
        return self._size

    def has_won(self):
        for item in self._card_array.flat:
            if not(item._front_up):
                return False
        return True
