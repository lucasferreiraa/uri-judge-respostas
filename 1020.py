# -*- coding: utf-8 -*-
# URI Judge - Problema 1020

idade = int(input())

ano = idade / 365
idade = idade % 365
mes = idade / 30
dias = idade % 30

print(int(ano), "ano(s)")
print(int(mes), "mes(es)")
print(int(dias), "dia(s)")
