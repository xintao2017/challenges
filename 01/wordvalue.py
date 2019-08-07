from data import DICTIONARY, LETTER_SCORES



def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY, 'r') as dictionary:
        for line in dictionary:
            words.append(line.rstrip())
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(k.upper(), 0) for k in word])

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
