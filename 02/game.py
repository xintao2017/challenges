#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
import itertools

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Return a random list of 7 Capital letters . Fetch letters from POUCH"""
    return random.choices(POUCH, k=7)


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_possible_dict_words(letters):
    """Get all possible words from letters and words must in DICTIONARY"""
    words = []
    print(letters)
    for word in DICTIONARY:
        if len(word) < NUM_LETTERS and all([l in letters for l in word.upper()]):
            if all(letters.count(x) >= word.upper().count(x) for x in word.upper()):
                words.append(word)
    return words


def _get_permutations_draw(letters):
    """Get a shuffled list of letters"""
    print(list([itertools.permutations(letters, n) for n in range(1, NUM_LETTERS + 1)]))
    return [itertools.permutations(letters, n) for n in range(1, NUM_LETTERS + 1)]


def _validation(*args, **kwds):
    if args[0] is args[1]:
        pass
    else:
        raise ValueError("Inputs do not match with each other.")


def main():
    pass


if __name__ == "__main__":
    main()
