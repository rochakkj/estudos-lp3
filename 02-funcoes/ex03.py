#Ex03 - Contador de Vogais e Consoantes:
vogais = ["a", "e", "i", "o", "u"]
consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]


def fraseUsuario():
    fraseUsuario = (input("Digite uma frase: "))
    fraseUsuario = fraseUsuario.lower()
    return fraseUsuario.lower()

def contaVogaisConsoantes(fraseUsuario):
    numVogais = 0
    numConsoantes = 0
    for caracter in fraseUsuario:
        if  caracter in vogais:
            numVogais = numVogais + 1
        elif caracter in consoantes:
            numConsoantes = numConsoantes + 1

    print(f"Vogais = {numVogais}\nConsoantes = {numConsoantes}")

def main():
    contaVogaisConsoantes(fraseUsuario())

main()
