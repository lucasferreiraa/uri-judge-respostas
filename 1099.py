# -*- coding: utf-8 -*-
# URI Judge - Problema 1099

limite = int(input())

aux = 0
soma = 0

while aux<limite:
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    aux += 1
    
    if (a < b):
        for i in range(a+1,b):
            if (i % 2 == 1):
                soma += i
        print(soma)
        soma = 0
    elif (a > b):
        for i in range(b+1,a):
            if (i % 2 == 1):
                soma += i
        print(soma)
        soma = 0
    else:
        print(0)
