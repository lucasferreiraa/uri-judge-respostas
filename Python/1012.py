# -*- coding: utf-8 -*-
# URI Judge - Problema 1012

pi = 3.14159
a, b, c = map(float, input().split())

triangulo = (c * a) / 2
circulo = pi * (c ** 2)
trapezio = ((a + b) / 2) * c
quadrado = b ** 2
retangulo  = a * b

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)
