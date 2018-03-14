# -*- coding: utf-8 -*-
#URI Judge - Problema 1036

a, b, c = map(float, input().split())

if a == 0 or b == 0 or c == 0:
    print("Impossivel calcular")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Impossivel calcular")
    elif delta >= 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)   
        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
