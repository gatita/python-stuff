#!/usr/bin/env python

from string import maketrans

def rot13(text):
    original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    cyphered = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    table = maketrans(original, cyphered)
    return text.translate(table)

test rot13 encryption
if __name__ == '__main__':
    assert rot13('hi') == 'uv'
    assert rot13('HI') == 'UV'
    assert rot13('Hey there, friend!') == ('Url gurer, sevraq!')
    assert rot13(rot13('hi')) == 'hi'
    print 'Looks good'
