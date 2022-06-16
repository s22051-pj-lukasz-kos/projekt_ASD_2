import calc_code
import find_freq
import huffman
import compress_text
from Node import Node

# Przeliczanie ilości znaków i generowanie dict
char_freq_fict = find_freq.find_freq('lorem.txt')
letters = char_freq_fict.keys()

# Tablica do przechowywania obiektów klasy Node.
# Node jest węzłem drzewa binarnego.
# Indeks 0 służy do przechowywania wielkości kopca (heapsize)
huffman_heap = [len(letters)]
for letter in letters:
    huffman_heap.append(Node(char_freq_fict.get(letter), letter))

# Generowanie drzewa binarnego
huffman.huffman(huffman_heap)

# Generowanie kodów Huffmana
huffman_encoding = calc_code.calc_code(huffman_heap[1])

# Generowanie skompresowanego tekstu
compress_text.compress_text('lorem.txt', 'lorem_compress.txt', huffman_encoding)
