

def volume_aquario(altura: int | float, comprimento: int | float, largura: int | float):
    return ((altura * largura * comprimento) / 1000)

def potencia_termostato(altura: int | float, comprimento: int | float, largura: int | float, temperatura_desejada : float, temperatura_ambiente = 25):
    return volume_aquario(altura, comprimento, largura) * 0.05 * (temperatura_desejada - temperatura_ambiente)

def quantidade_filtragem(altura: int | float, comprimento: int | float, largura: int | float):
    return (((altura * largura * comprimento) / 1000) * 2.5)

def main():

    comprimento = float(input("Digite o comprimento do aquário: "))

    altura = float(input("Digite a altura do aquário: "))

    largura = float(input("Digite a largura do aquário: "))

    temperatura_desejada = float(input("Digite a temperatura ideal para o aquário: "))



    print(f"O volume do aquário é {volume_aquario(comprimento, altura, largura)} litros")
    print(f"A potência do termostato necessária para manter a temperatura adequada dentro do aquário é {potencia_termostato(comprimento, altura, largura, temperatura_desejada)}")
    print(f"A quantidade em litros de filtragem por hora necessária para manter a qualidade da água é de {quantidade_filtragem(comprimento, altura, largura)} litros")

main()