#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

def solution_1(str, n):
    ret = []
    ascii_a = ord('a')
    ascii_z = ord('z')
    for c in str:
        ascii = ord(c)
        if ascii >= ascii_a and ascii <= ascii_z:
            ascii += n
            if ascii > ascii_z:
                ascii = ascii_a + (ascii - ascii_z - 1)
        ret.append(chr(ascii))
    return "".join(ret)

def solution_2(str, n):
    a_z = string.lowercase
    trantab = string.maketrans(a_z, a_z[n:] + a_z[:n])
    return str.translate(trantab)


if __name__ == '__main__':
    str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    str = "map"
    n = 2
    print 'solution 1:', solution_1(str, n)
    print 'solution 2:', solution_2(str, n)
