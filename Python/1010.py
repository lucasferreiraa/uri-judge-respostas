# -*- coding: utf-8 -*-
# URI Judge - Problema 1010

peca1 = input().split()
peca2 = input().split()

qtd1 = int(peca1[1])
preco1 = float(peca1[2])

qtd2 = int(peca2[1])
preco2 = float(peca2[2])

total = (qtd1 * preco1) + (qtd2 * preco2)

print("VALOR A PAGAR: R$ %.2f" % total)
