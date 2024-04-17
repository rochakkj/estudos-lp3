#Ex05 - Verificador de Palíndromos:


def palavraOriginal():
    palavra = list(input("Digite uma palavra: "))
    palavraOriginalList = []
    palavraOriginalList.extend(palavra)
    palavraOriginal = ""
    for caracter in palavraOriginalList:
        palavraOriginal += caracter
    return palavra
    

def palavraReversa(palavra):
    list(palavra)
    palavra.reverse()
    palavraReversaList = []
    palavraReversaList.extend(palavra)
    palavraReversa = ""
    for caracter in palavraReversaList:
        palavraReversa += caracter
    return palavraReversa


def verificaPalindromo(palavraReversa):

    if palavraOriginal.lower() == palavraReversa.lower():
        print(f"Palavra é palíndromo: {palavraOriginal.lower()}")

    else:
        print(f"Palavra não é palíndromo: {palavraOriginal.lower()} e {palavraReversa.lower()}")

def main():
    palavraOriginal()
    palavraReversa(palavraOriginal())
    verificaPalindromo(palavraOriginal(), palavraReversa())

main()