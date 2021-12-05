from app.common.constants import MORSE_CODE_DICT


class MorseController:
    __slots__ = ["morse_dict"]

    def __init__(self):
        self.morse_dict = MORSE_CODE_DICT

    def translate_word(self, word):
        word_translated = ""
        letters = word.split(" ")
        for letter in letters:
            word_translated = word_translated + str(self.morse_dict.get(letter))

        return word_translated
