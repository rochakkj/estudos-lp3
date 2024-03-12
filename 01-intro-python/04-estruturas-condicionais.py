# if
# Sintaxe:
#if condição:
#   código
#   código
#   código
# Sempre edentado (dois, quatro ou mais espaços)

num = 1
# if simples
if num == 1:
    print("Número correto")    

# if else

if num == 2:
    print("Número meio certo")

else:
    print("Número errado")

# elif
num1 = 100
if num1 < 10:
    print("Bebê\n")

elif num1 < 13:
    print("Criança\n")

elif num1 < 21:
    print("Adolencente\n")

elif num1 < 60:
    print("Adulto\n")

else:
    print("Idoso\n")