#abrir o arquivo

# arquivo = open("dados.txt")

#print(arquivo)
#conteudo = arquivo.read()
#print(conteudo)

#conteudos = arquivo.readlines()
#print(conteudos)
# linhas = []

# for linha in arquivo:
#     linhas.append(linha.strip())

# print(linhas)
# arquivo.close()

#bloco with
# with open("dados.txt") as arquivo2:
#      conteudo = arquivo2.read()
#      print(conteudo)


#alterar o arquivo
#w = substitui tudo no arquivo

# with open("dados.txt", "a") as arquivo3:
#      arquivo3.write("frutas")

#a = append adiciona ao arquivo

# with open("dados.txt", "a") as arquivo4:
#      arquivo4.write("\nfrutas")

# ler o arquivo produtos.cvs
# e carregar em memória na lista
# cada produtos sendo um dict

def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            dados = linha.strip().split(",")
            produto = {
                "nome": dados[0],
                "descricao": dados[1],
                "preco": dados[2],
                "imagem": dados[3]

            }
            produtos.append(produto)

    return produtos


def salvar_produto(nome, descricao, preco, imagem):
    texto = f"\n{nome},{descricao},{preco},{imagem}"
    with open("produtos.csv", "a") as arquivos_produtos:
        arquivos_produtos.write(texto)


salvar_produto("H20", "lata", "1.25", "h20.jpg")
salvar_produto("Monster", "lata", "5.0", "monster.jpg")


print(obter_produtos())