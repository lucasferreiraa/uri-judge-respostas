# -*- coding: utf-8 -*-
# URI Judge - Problema 1044

valores = input().split()

a = int(valores[0])
b = int(valores[1])

if a % b == 0:
    print("Sao Multiplos")
elif b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
