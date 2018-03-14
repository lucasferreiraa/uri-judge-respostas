# -*- coding: utf-8 -*-
# URI Judge - Problema 1013

a, b, c = map(int, input().split())

if a > (b and c):
    print(str(a) + " eh o maior")
elif b > c:
    print(str(b) + " eh o maior")
else:
    print(str(c) + " eh o maior")
