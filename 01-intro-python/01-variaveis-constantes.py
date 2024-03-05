#identificadores
    #letras, números e _

    #case sensitive (maiúsculo e minúsculo diferem variáveis) Ex:
Num = 1
num = 2

    #palavras reservadas(não podem ser usadas como identificadores): def, if, for, ...

    #"Formatação" identificador = valor(literal) Ex:
nome = "Jorge"
num = 3
num = True

#constante
    #não existem no python

#comentário uma linha <-

"""

Várias linhas

"""

#docstring
    #comentário no começo da função documentando(a explicando)
    #classes, módulos, etc
def numero (v, v1):
    """
    printa oi
    """
    print ("oi")
    return v + v1

numero(3, 4.1)
