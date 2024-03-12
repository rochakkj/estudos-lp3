# Operadores aritméticos
# +, -, *, /, **, ...

nota1 = 6.0
nota2 = 3.0
nota3 = 1.0

media = (nota1 + nota2 + nota3)/3
print(media)

# Operadores Lógicos
# and, or, not

print (True and True) #True
print (True and False) #False
print (False and True) #False
print (False and False) #False

# Liberação

# Exemplo
# Permitir entrada caso:
# Jogo online, email válido, conta desbanida

JogoOnline = True
Email = ["5@gmail.com", "4@gmail.com", "3@gmail.com", "2@gmail.com", "1@gmail.com"]
ContaBan = False
EmailUser = "5@gmail.com"
EmailValid = EmailUser in Email
                

if (JogoOnline and not ContaBan and EmailValid):
    print("Acesso liberado!")
    
    
#Operadores de comparação 
# >, <, >=, <=, ==, !=
# = atribui valor
# == compara valores
# != diferente

# is, is not
# operador de identidade
# compara se objetos ocupam o mesmo espaço na memória


# operador in, not in
# verifica se um elemento existe ou não em uma sequência
#str, list, tuple