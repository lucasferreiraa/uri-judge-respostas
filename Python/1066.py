# -*- coding: utf-8 -*-
# URI Judge - Problema 1066

par = 0
impar = 0
positivo = 0
negativo = 0
count = 0

while count < 5:
    num = int(input())
    count += 1

    if (num % 2 == 0):
        par += 1
    if (num % 2 != 0):
        impar += 1
    if (num > 0):
        positivo += 1
    if (num < 0):
        negativo += 1

print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")
print(str(positivo) + " valor(es) positivo(s)")
print(str(negativo) + " valor(es) negativo(s)")