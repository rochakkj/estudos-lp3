# Função

# Quero somar dois números
# usar função sum()
 
# Quero calcular média dos alunos
# tem no python?
# alguém já programou (copiar / adicionar dependência)


# Declaração

#def nome_funcao(parametro, parametro, ...)


# Chamada

print("Olá")
sum([1, 3])

# Função sem retorno e sem parâmetros

def imprimi_furia():
    print("Furia!")

imprimi_furia()

# Função sem retorno e com parâmetros

def escalacao(nomes):
    print(nomes)

def time(nome_time, escalacao_time):
    return nome_time, escalacao_time
furia = ["fallen", "chelo", "kscerato", "yurihh", "art"]
escalacao(time("Furia", furia))
          
# Função com retorno e sem parâmetros
def status_furia():
    return "Venceu!"


print(status_furia())


# Função com retorno e com parâmetros

def gerar_escalacao(nomes):
    return f"{nomes}"
print(gerar_escalacao(furia))


def saudacao(nome1, frase):
    return f"{frase} {nome1}"


print(time("Furia", furia))





# entrada

notas_alunos = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 7.0],
    [9.0, 1.0, 3.0]
]

def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_media_alunos(notas_alunos):
    return [calcular_media(notas) for notas in notas_alunos]

medias = calcular_media_alunos(notas_alunos)
print(medias)