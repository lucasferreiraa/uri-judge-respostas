# -*- coding: utf-8 -*-
# URI Judge - Problema 1060

flag = 0
positivo = 0
negativo = 0

while flag < 6:
    
    num = input()
    
    if num >= 0:
        positivo += 1
    else:
        negativo += 1
    
    flag += 1

print(str(positivo) + " valores positivos")
