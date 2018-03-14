# -*- coding: utf-8 -*-
# URI Judge - Problema 1018

valor = int(input())
print(valor)

cem = valor / 100
valor = valor % 100
cinquenta = valor / 50
valor = valor % 50
vinte = valor / 20
valor = valor % 20
dez = valor / 10
valor = valor % 10
cinco = valor / 5
valor = valor % 5
dois = valor / 2
valor = valor % 2
um = valor / 1

print(int(cem), "nota(s) de R$ 100,00")
print(int(cinquenta), "nota(s) de R$ 50,00")
print(int(vinte), "nota(s) de R$ 20,00")
print(int(dez), "nota(s) de R$ 10,00")
print(int(cinco), "nota(s) de R$ 5,00")
print(int(dois), "nota(s) de R$ 2,00")
print(int(um), "nota(s) de R$ 1,00")
