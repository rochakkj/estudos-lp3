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

# Operador ternário

idade = 17

status = "Maior" if idade >= 18 else "Menor"

print(status)


# Match

dia = 5

match dia:

    case 1:
        print("Hoje é domingo")
    case 2:
        print("Hoje é segunda")
    case 3:
        print("Hoje é terça")
    case 4:
        print("Hoje é quarta")
    case 5:
        print("Hoje é quinta")
    case 6:
        print("Hoje é sexta")
    case 7:
        print("Hoje é sábado")
    case _:
        print("Hoje não é")


match dia:

    case 1 | 7:
        print("Fds")

    case 2 | 3 | 4 | 5 | 6:
        print("Não é fds")

    case _:
        print("Não é")
    

