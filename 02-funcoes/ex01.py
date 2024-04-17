#Ex01 - Jogo de Adivinhação:
import random

numAleatorio = random.randint(1, 100)

def acertos():
    
    print(f"Acertou! O número era {numAleatorio}")

def erros():
    chuteUsuario = int(input("Digite seu chute: ")) - numAleatorio
    while chuteUsuario != 0:
        while chuteUsuario < 0:
                chuteUsuario = int(input("Errou! É maior que isso: ")) - numAleatorio
        while chuteUsuario > 0:
                chuteUsuario = int(input("Errou! É menor que isso: ")) - numAleatorio

def main():
      erros()
      acertos()

main()