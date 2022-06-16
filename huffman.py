import heap
from Node import Node
import priority_queue


# Algorytm Huffmana do generowania drzewa binarnego.
# Operuje on na kopcu obiektów klasy Node.
# W oprarciu o to drzewo można wygenerować kody Huffmana.
def huffman(tab):
    tab_length = len(tab) - 1
    heap.build_min_heap(tab)

    for index in range(1, tab_length):
        left_child_node = priority_queue.heap_extract_min(tab)
        right_child_node = priority_queue.heap_extract_min(tab)
        left_child_node.code = 0
        right_child_node.code = 1
        freq = left_child_node.freq + right_child_node.freq
        name = left_child_node.char + right_child_node.char
        new_node = Node(freq, name, left_child_node, right_child_node)
        priority_queue.min_heap_insert(tab, new_node)
    return priority_queue.heap_extract_min(tab)
