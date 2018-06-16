# -*- coding: utf-8 -*-
# URI Judge - Problema 1073

entrada = int(input())

for i in range(1, entrada+1):
    if (i % 2 == 0):
        print(str(i) + "^2 = " + str(i**2))
    else:
        pass