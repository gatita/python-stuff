#!/usr/bin/env python

from string import maketrans

def rot13(text):
    original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    cyphered = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    table = maketrans(original, cyphered)
    return text.translate(table)
