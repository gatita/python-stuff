#!/usr/bin/env python

from io import open
import random

def read_book(textfile):
    """ open text file and return contents as a string """
    f = open(textfile, encoding='utf-8')
    text = " ".join(f.readlines())
    return text.split()

def create_trigram(words):
    """ create trigram dictionary """
    myDict = {}
    for i in range(len(words)-2):
        myKey = tuple(words[i:i+2])
        myValue = words[i+2]
        myDict.setdefault(myKey, []).append(myValue)
    return myDict
    
def generate_text(trigram):
    """ Generate new text from trigram dictionary. """
    myText = ""
    newText = random.choice(trigram.keys())
    myText += ' '.join(newText)
    myText = myText[:1].upper() + myText[1:]
    myText += ' ' + str(random.choice(trigram[newText]))
    while len(myText.split()) < 200:
        newText = tuple(myText.split()[-2:])
        if newText in trigram:
            myText += ' ' + str(random.choice(trigram[newText]))
            if myText[-1] == '.':
                newText = random.choice(trigram.keys()) 
        else:
            newText = random.choice(trigram.keys())
            myText += ' ' + ' '.join(newText)
    if myText[-1] != '.':
        myText += '.'
    return str(myText)
    
    
    
    
# words = readBook('sherlock_small.txt')
# trigram = create_trigram(words)
# generate_text(trigram)

