# Funkcje do tworzenia kopców binarnych typu min
# Kopiec składa się z obiektów klasy Node
# Komórka o indeksie 0 przechowuje wielkość kopca heapsize
# Kopiec zaczyna się od indeksu 1

# szukanie rodziców i dzieci
def parent(index):
    return index // 2


def left(index):
    return 2 * index


def right(index):
    return 2 * index + 1


# przywracanie własności kopca typu min
def min_heapify(tab, index):
    heapsize = tab[0]
    left_child = left(index)
    right_child = right(index)
    smallest = index

    if left_child <= heapsize and tab[left_child].freq < tab[smallest].freq:
        smallest = left_child

    if right_child <= heapsize and tab[right_child].freq < tab[smallest].freq:
        smallest = right_child

    if smallest != index:
        tab[index], tab[smallest] = tab[smallest], tab[index]
        min_heapify(tab, smallest)


# budowanie kopca typu min
def build_min_heap(tab):
    # ustalanie wielkości kopca
    tab[0] = len(tab) - 1
    start = tab[0] // 2
    for index in range(start, 0, -1):
        min_heapify(tab, index)
