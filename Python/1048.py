# -*- coding: utf-8 -*-
# URI Judge - Problema 1048

salario = float(input())

if salario <= 400:
    reajuste = salario * 0.15
    novosalario = salario + reajuste
    print("Novo salario: %.2f" % novosalario)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 15 %")

elif salario > 400 and salario <= 800:
    reajuste = salario * 0.12
    novosalario = salario + reajuste
    print("Novo salario: %.2f" % novosalario)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 12 %")

elif salario > 800 and salario <= 1200:
    reajuste = salario * 0.10
    novosalario = salario + reajuste
    print("Novo salario: %.2f" % novosalario)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 10 %")

elif salario > 1200 and salario <= 2000:
    reajuste = salario * 0.07
    novosalario = salario + reajuste
    print("Novo salario: %.2f" % novosalario)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 7 %")

elif salario > 2000:
    reajuste = salario * 0.04
    novosalario = salario + reajuste
    print("Novo salario: %.2f" % novosalario)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 4 %")
