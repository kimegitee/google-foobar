#!/usr/bin/python

CAP_MARK = "cap_mark"

def make_braille_dict():
    a_list = list("The quick brown fox jumped over the lazy dogs".lower())
    a_list.insert(0, CAP_MARK)
    b_string = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110011100"
    b_list = [b_string[i: i + 6] for i in range(0, len(b_string), 6)]
    return dict(zip(a_list, b_list))

def look_up(c, d):
    if c.isupper():
        return look_up(CAP_MARK, d) + look_up(c.lower(), d)
    else:
        return d[c]

def answer(plaintext):
    return "".join([look_up(c, make_braille_dict()) for c in list(plaintext)])