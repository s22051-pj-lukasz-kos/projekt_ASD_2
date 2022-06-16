# Algorytm Huffmana korzysta z kolejki priorytetowej typu min
# zaimplementowanej jako kopiec binarny typu min.
# Komórka o indeksie 0 przechowuje wielkość kopca.
# Kopiec zaczyna się od indeksu 1.
import math
import heap
from Node import Node


# Element kopca binarnego tab o najmniejszym kluczu.
# Klucz to wartość, którą należy posortować względem pozostałych kluczy.
def heap_minimum(tab):
    return tab[1]


# Usuwa i zwraca z kopca binarnego element o najmniejszym kluczu.
def heap_extract_min(tab):
    heapsize = tab[0]
    if heapsize > 0:
        minimum = tab[1]
        tab[1] = tab[heapsize]
        heapsize -= 1
        tab[0] = heapsize
        heap.min_heapify(tab, 1)
        return minimum


# Zmienia wartość klucza elementu o indeksie 'index' na nową wartość 'key'.
# 'key' nie może być większa niż aktualna wartość klucza o indeksie 'index'.
# Klucz to wartość, którą należy posortować względem pozostałych kluczy.
# W przypadku kodów Huffmana będzie to częstotliwość występowania (freq)
def heap_decrease_key(tab, index, key):
    if key.freq <= tab[index].freq:
        tab[index] = key
        while index > 1 and tab[heap.parent(index)].freq > tab[index].freq:
            tab[index], tab[heap.parent(index)] = tab[heap.parent(index)], tab[index]
            index = heap.parent(index)


# Wstawia element o kluczu 'key' do kopca tab.
def min_heap_insert(tab, key):
    # w komórce 0 trzymana jest wielkość kopca
    tab[0] += 1
    heapsize = tab[0]
    tab[heapsize] = Node(math.inf, '')
    heap_decrease_key(tab, heapsize, key)
