# -*- coding: utf-8 -*-
#URI Judge - Problema 1065

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

### 1 valor par ###
if (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("1 valor par")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("1 valor par")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("1 valor par")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 != 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("1 valor par")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("1 valor par")

### 2 valores pares ###
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 != 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("2 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("2 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("2 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("2 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 != 0) and (n4 % 2 == 0) and (n5 %2 == 0):
	print("2 valores pares")

### 3 valores pares ###
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 != 0):
	print("3 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("3 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 != 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("3 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("3 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("3 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("3 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("3 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 == 0):
	print("3 valores pares")

### 4 valores pares ###
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 != 0):
	print("4 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 != 0) and (n5 %2 == 0):
	print("4 valores pares")
elif (n1 % 2 == 0) and (n2 % 2 != 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 == 0):
	print("4 valores pares")
elif (n1 % 2 != 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 == 0):
	print("4 valores pares")

### 5 valores pares ###
elif (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) and (n4 % 2 == 0) and (n5 %2 == 0):
	print("5 valores pares")