# -*- coding: utf-8 -*-
# URI Judge - Problema 1040

nota1, nota2, nota3, nota4 = map(float, input().split())

media  = ((nota1 * 2.0) + (nota2 * 3.0) + (nota3 * 4.0) + (nota4 * 1.0)) / 10.0

if media >= 5 and media < 7:
    print("Media: %.1f" % media)
    print("Aluno em exame.")

    exame = float(input())
    final = (media + exame) / 2
    
    if final >= 5:
        print("Nota do exame: %.1f" % exame)
        print("Aluno aprovado.")
        print("Media final: %.1f" % final)
    else:
        print("Nota do exame: %.1f" % exame)
        print("Aluno reprovado.")
        print("Media final: %.1f" % final)

elif media >= 7:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")

else:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
