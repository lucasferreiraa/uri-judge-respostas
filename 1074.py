# -*- coding: utf-8 -*-
# URI Judge - Problema 1074

entrada = int(input())
count = 0

while count < entrada:
    num = int(input())
    count += 1
    if (num % 2 == 0 and num > 0):
        print("EVEN POSITIVE")
    elif (num % 2 != 0 and num > 0):
        print("ODD POSITIVE")
    elif (num % 2 == 0 and num < 0):
        print("EVEN NEGATIVE")
    elif (num % 2 != 0 and num < 0):
        print("ODD NEGATIVE")
    else:
        print("NULL")