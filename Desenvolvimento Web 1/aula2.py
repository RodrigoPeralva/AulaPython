#1 Questão
nome = input("Escreva seu nome: ")
nota_1 = input("Escreva sua 1 nota:")
nota_2 = input("Escreva sua 2 nota:") 
nota_3 = input("Escreva sua 3 nota:")

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)

media = (nota_1 + nota_2 + nota_3)/3

if media >= 6.0:
    print("Aluno aprovado.")
elif media >= 5 and media < 6:
    print("Aluno de recuperação.")
elif media < 5:
    print("Aluno reprovado.")

#2 Questão
nome = input("Escreva seu nome: ")
nota_1 = input("Escreva sua 1 nota:")
nota_2 = input("Escreva sua 2 nota:") 
nota_3 = input("Escreva sua 3 nota:")

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)

media = (nota_1 + nota_2 + nota_3)/3

if media >= 9.5:
    print("Nota A.")
elif media < 9.5 and media >= 8.5:
    print("Nota B.")
elif media < 8.5 and media >= 7.5:
    print("Nota C.")
elif media < 7.5 and media >= 6:
    print("Nota D.")
elif media < 6 and media >= 5:
    print("Nota E.")
elif media < 5 and media >= 0:
    print("Nota F.") 

#3 Questão
nome = input("Escreva seu nome: ")
nota_1 = input("Escreva sua 1 nota:")
nota_2 = input("Escreva sua 2 nota:") 
nota_3 = input("Escreva sua 3 nota:")

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)

media = (nota_1 + nota_2 + nota_3)/3

if media >= 9.5:
    print("Nota A aprovado.")
elif media < 9.5 and media >= 8.5:
    print("Nota B aprovado.")
elif media < 8.5 and media >= 7.5:
    print("Nota C aprovado.")
elif media < 7.5 and media >= 6:
    print("Nota D aprovado.")
elif media < 6 and media >= 5:
    print("Nota E recuperação.")
elif media < 5 and media >= 0:
    print("Nota F reprovado.") 