

str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'
str = 'map'
result = ''
for i in str:
    if i >= 'a' and i <= 'x':
        i = ord(i)
        i = i + 2
        i = chr(i)
        result += i
    elif i is 'y':
        result += 'a'
    elif i is 'z':
        result += 'b'
    else:
        result += i

print(result)
