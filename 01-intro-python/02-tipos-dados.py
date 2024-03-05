#Tipos de dados

    #int, float
    #string, list, tuple, set
    #dict
    #none


    #int
num = 1

    #float
num1 = 1.1

    #string
nome = "boungiourno"
print (nome[0])
print (nome[-1])
print (nome[0:3])

    #nome = objeto da classe str
    #nome.(métodos da str) Ex:
print(nome.capitalize()) #primeira letra do string maiúscula   

    #interpolação de str w varíaveis
    #f-string
msg = f"Olá seu nome é {nome.capitalize()} e tem {num1} anos"
print(msg)

    #list
    #lista de valores
    #pode ser alterada
hability = []
hability = ["1", "2", "3.1", "4,2", "jorginho"]
print(hability)
print(hability[0])
print(hability[1])
print(hability[-1].capitalize())

hability[1] = 2.1
print(hability[1])
hability.append("jorjão") #inseri string no último posição da lista (cria uma posição a mais)
hability.insert(1, "jorjin") #inseri um string em uma posição específica da lista, e move todos os itens uma casa
print(hability[1])


print(hability)

    #tuple
    #lista que não pode ser alterada após criada
habili = (1, 2, 3)

    #for
for habil in habili:
    print(habil)

    # set
    # não indexado
    # não permite elementos duplicados
    # digite mensagens
    # digite os emails de destino
emails = {"davi@gmail.com", "rocha@gmail.com", "davi@gmail.com"}
emails.add("davi@gmail.com")
print(emails)

    #dict
    #dicionário
    #chave : valor
    #key : value
    #vaga
vaga = {
    "empresa" : "quickmotors",
    "título" : "Mecânico de software",
    "salario" : 150.0,
    "mecanicoMain" : False
}
print(vaga)




