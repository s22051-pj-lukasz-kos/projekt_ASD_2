# Program kompresuje tekst na podstawie kodów Huffmana

def compress_text(read_file, write_file, huffman_encoding):
    # plik do odczytu
    read_f = open(read_file)

    # plik do zapisu tekstowego
    write_text_file = open(write_file, 'wt')

    # zapisuje jawnie słownik na początku pliku
    for elem in dict(sorted(huffman_encoding.items(), key=lambda item: item[0])):
        write_text_file.writelines(elem + ': ' + huffman_encoding.get(elem) + '\n')
    write_text_file.writelines('\n\n')
    write_text_file.close()

    # zapisuje tekst z pliku źródłowego jako skompresowany tekst binarny
    result = ''
    for c in read_f.read():
        result += huffman_encoding.get(c)
    with open(write_file, 'ab') as write_binary_file:
        write_binary_file.write(to_bytes(result))

    read_f.close()


# funkcja do konwersji binarnego zapisu w string na typ bytearray
def to_bytes(data):
    b = bytearray()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i + 8], 2))
    return bytes(b)
