# -*- coding: utf-8 -*-
# URI Judge - Problema 1019

tempo = int(input())

hora = tempo / 3600
tempo = tempo % 3600
minuto = tempo / 60
tempo = tempo % 60
segundo = tempo / 60
tempo = tempo % 60

print("%d:%d:%d" % (hora, minuto, tempo))
