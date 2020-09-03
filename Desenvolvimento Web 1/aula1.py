#1 atividade
frase = input("Escreva uma frase: ")

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

#2 atividade
nota_1, peso_1 = "9.5,3".split(",", 2)

print(nota_1)
print(peso_1)

# 1 questão
s = True
n = False

res_1 = s and s
res_2 = s and n
res_3 = n and s
res_4 = n and n

print(res_1,res_2,res_3,res_4)

res_1 = s or s
res_2 = s or n
res_3 = n or s
res_4 = n or n

print(res_1,res_2,res_3,res_4)

res_1 = not s
res_3 = not n

print(res_1,res_3)

# 2 questão
num_1 = int(input("Escreva o 1 número inteiro: "))
num_2 = int(input("Escreva o 2 número inteiro: "))

resultado = (num_1 + num_2)/2
print(resultado)

# 3 questão
num_1, peso_1 = input("Escreva o 1 número e o seu peso separados por ',': ").split(",", 2)
num_2, peso_2 = input("Escreva o 2 número e o seu peso separados por ',': ").split(",", 2)

num_1 = float(num_1)
num_2 = float(num_2)
peso_1 = int(peso_1)
peso_2 = int(peso_2)

resultado = ((num_1 * peso_1) + (num_2 * peso_2))/(peso_1 + peso_2)

print(resultado)

# 4 questão
nome = input("Escreva seu nome: ")
nota_1 = input("Escreva sua 1 nota:")
nota_2 = input("Escreva sua 2 nota:") 
nota_3 = input("Escreva sua 3 nota:")

nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)

media = (nota_1 + nota_2 + nota_3)/2

print("Sua media é " + media)

# 5 questão
nome = input("Escreva seu nome: ")
nota_1, peso_1 = input("Escreva sua 1 nota e o seu peso separados por ',':").split(",",2)
nota_2, peso_2 = input("Escreva sua 2 nota e o seu peso separados por ',':").split(",",2)

media_ponderada = (nota_1 + nota_2)/(peso_1 + peso_2)

print("A sua media ponderada é: "+ media_ponderada)

# 6 questão

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

delta = b**2 - 4*a*c

x1 = (-b + (delta*(1/2)))/(2*a)

x2 = (-b - (delta*(1/2)))/(2*a)

print("O valor de x1 {} e o valor de x2 {}".format(x1,x2))