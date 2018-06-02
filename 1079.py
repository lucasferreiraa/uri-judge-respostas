# -*- coding: utf-8 -*-
# URI Judge - Problema 1079

num = int(input())
count = 0

while count < num:
    numeros = input().split()
    n1 = float(numeros[0])
    n2 = float(numeros[1])
    n3 = float(numeros[2])

    result = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

    print("%.1f" % result)

    count += 1