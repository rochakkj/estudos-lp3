#Ex02 - Tabuada de Um Número:



def numDigitado():
    numTabuada = int(input("Digite um número de 1 a 10: "))
    while numTabuada < 1 or numTabuada > 10:
        numTabuada = int(input("Número inválido, digite um número entre 1 e 10: "))
    return numTabuada

def tabuada(numTabuada):
    n = 1
    print(f"Tabuada do {numTabuada}")
    while n <= 10:
        resul = n * numTabuada
        print(f"{n} X {numTabuada} = {resul}")
        n = n + 1


def main():
    tabuada(numDigitado)

main()