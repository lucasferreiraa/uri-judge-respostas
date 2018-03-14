# -*- coding: utf-8 -*-
# URI Judge - Problema 1038

menu = {'cachorro':4.00, 'xsalada':4.50, 'xbacon':5.00, 'torrada':2.00, 'refri':1.50}

codigo, quantidade = map(int, input().split())

if codigo == 1:
    total = menu['cachorro'] * quantidade
    print("Total: R$ %.2f" % total)
elif codigo == 2:
    total = menu['xsalada'] * quantidade
    print("Total: R$ %.2f" % total)
elif codigo == 3:
    total = menu['xbacon'] * quantidade
    print("Total: R$ %.2f" % total)
elif codigo == 4:
    total = menu['torrada'] * quantidade
    print("Total: R$ %.2f" % total)
elif codigo == 5:
    total = menu['refri'] * quantidade
    print("Total: R$ %.2f" % total)
