# -*- coding: utf-8 -*-
# URI Judge - Problema 1035

a, b, c, d = map(int, input().split())

somaab = a + b
somacd = c + d

if (b > c) and (d > a) and (somacd > somaab) and ((c and d) % 2 == 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
