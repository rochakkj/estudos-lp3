# Ex3

compra = float(input("Digite o valor da compra: R$"))

if compra < 10:
    desc = 0

elif compra < 100:
    desc = 0.05

elif compra < 500:
    desc = 0.1

else:
    desc = 0.15

valorf = compra - (compra * desc)

print(f"O valor final é R${valorf}\nO valor descontado foi de R${compra * desc}\nO desconto foi de {desc * 100}%")