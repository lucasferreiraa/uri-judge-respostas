# -*- coding: utf-8 -*-
# URI Judge - Problema 1045

num1, num2, num3 = map(float, input().split())
valores = []

valores.append(num1)
valores.append(num2)
valores.append(num3)
valores.sort(reverse=True)

a = valores[0]
b = valores[1]
c = valores[2]

if (a >= (b + c)) == False:
    if (a**2) == ((b**2) + (c**2)):
        print("TRIANGULO RETANGULO")
    if (a**2) > ((b**2) + (c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2) < ((b**2) + (c**2)):
        print("TRIANGULO ACUTANGULO")
    if (a == b) and (a == c) and (b == c):
        print("TRIANGULO EQUILATERO")
    if ((a == b) and (a != c) and (b != c)) or ((a == c) and (a != b) and (c != b)) or ((b == c) and (b != a) and (c != a)):
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")
