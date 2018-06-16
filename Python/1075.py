# -*- coding: utf-8 -*-
# URI Judge - Problema 1075

num = int(input())

for i in range(1, 10000+1):
    if (i % num == 2):
        print(i)
