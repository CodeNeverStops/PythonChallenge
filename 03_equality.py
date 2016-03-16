#!/usr/bin/env python
# -*- encoding: utf-8 -*-
def convert(char):
    if char.islower():
        return 's'
    elif char.isupper():
        return 'B'
    else:
        return char

def solution_1(content):
    ret = []
    sB_text = "".join(map(convert, content))
    strlen = len(content)
    for i in range(strlen - 8):
        if sB_text[i:i+9] in ["\nBBBsBBBs", "sBBBsBBBs", "sBBBsBBB\n"]:
            ret.append(content[i:i+9])

    print "".join([c[len(c) / 2] for c in ret])

def solution_2(content):
    pass

content = file('03_equality.txt').read()
solution_1(content)
