# -*- coding: utf-8 -*-
# URI Judge - Problema 1070

num = int(input())
count = 0

while count < 6:
    if (num % 2 == 0):
        pass
        num += 1
    elif (num % 2 != 0):
        print(num)
        count += 1
        num += 1