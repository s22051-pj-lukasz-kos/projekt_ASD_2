# Program do generowania kodów Huffmana w oparciu o stworzone drzewo binarne
codes = {}


def calc_code(node, val=''):

    new_val = val + str(node.code)

    if node.left:
        calc_code(node.left, new_val)
    if node.right:
        calc_code(node.right, new_val)

    if not node.left and not node.right:
        codes[node.char] = new_val

    return codes
