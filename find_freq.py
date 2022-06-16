# Program generuje dict znaków znajdujących się w tekście
# znak: częstotliwość występowania w tekście

def find_freq(read_file):
    with open(read_file) as f:
        text = f.read()

    char_map = {}

    for letter in text:
        if letter in char_map:
            char_map[letter] += 1
        else:
            char_map[letter] = 1

    return char_map
