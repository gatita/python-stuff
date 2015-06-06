import pytest

from rot13 import rot13


def test_encryption():
    assert rot13('hi') == 'uv'
    assert rot13('HI') == 'UV'
    assert rot13('Hey there, friend!') == ('Url gurer, sevraq!')

def test_decryption():
    assert rot13(rot13('hi')) == 'hi'

