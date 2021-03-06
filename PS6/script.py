#!/usr/bin/python
import string

def buildCoder(shift):
    lc = list(string.ascii_lowercase)
    uc = list(string.ascii_uppercase) 
    c1 = list(''.join(lc[shift:])+''.join(lc[:shift+1]))
    c2 = list(''.join(uc[shift:])+''.join(uc[:shift+1]))
    d1 = {}
    for i in xrange(26):
        d1[uc[i]] = c2[i]
    for i in xrange(26):
        d1[lc[i]] = c1[i]
    return d1

def applyCoder(text, coder):
    cipher = ""
    for l in text:
        if l in string.ascii_lowercase or l in string.ascii_uppercase:
            cipher = cipher + str(coder[l])
        else:
            cipher = cipher + l
    return cipher

def applyShift(text, shift):
    after_shift = applyCoder(text, buildCoder(shift))
    print after_shift

applyShift('This is a test.', 8)
applyShift('Bpqa qa i bmab.', 18)
