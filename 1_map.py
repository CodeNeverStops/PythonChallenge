#!/usr/bin/python

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str = "map"
ret = []
for c in str:
    ascii = ord(c)
    ascii_a = ord('a')
    ascii_z = ord('z')
    if ascii >= ascii_a and ascii <= ascii_z:
        ascii += 2
        if ascii > ascii_z:
            ascii = ascii_a + (ascii - ascii_z - 1)
    ret.append(chr(ascii))

print "".join(ret)


