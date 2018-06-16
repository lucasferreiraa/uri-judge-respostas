# -*- coding: utf-8 -*-
# URI Judge - Problema 1046

inicio, fim = map(int, input().split())

if (inicio > fim):
    tempo = (24 + fim) - inicio
    print("O JOGO DUROU %d HORA(S)" % tempo)
elif (inicio < fim):
    tempo = fim - inicio
    print("O JOGO DUROU %d HORA(S)" % tempo)
else:
    print("O JOGO DUROU 24 HORA(S)") 
