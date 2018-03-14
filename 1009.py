# -*- coding: utf-8 -*-
# URI Judge - Problema 1009

funcionario = input()
salario_base = float(input())
vendas = float(input())

comissao = vendas * 0.15
salario_final = salario_base + comissao

print("TOTAL = R$ %.2f" % salario_final)
