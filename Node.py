# Klasa Node wykorzystywana w algorytmie Huffmana
# jako węzeł drzewa binarnego.


class Node:
    def __init__(self, freq, char, left=None, right=None):
        # częstotliwość znaków
        self.freq = freq

        # znak (litera)
        self.char = char

        # lewe dziecko
        self.left = left

        # prawe dziecko
        self.right = right

        # kod Huffmana
        self.code = ''
