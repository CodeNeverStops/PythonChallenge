#!/usr/bin/env python
# -*- coding: utf-8 -*-
def solution(content):
    chars = [char for char in content if char.isalpha()]
    print "".join(chars)

content = file('02_ocr.txt').read()
solution(content)

