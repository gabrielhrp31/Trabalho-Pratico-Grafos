# encoding: utf-8
num_nos = 0
num_arcos = 0
grafo = ""
source = []
sink = []

# funcao pra gerar matriz como a matriz é quadrada recebe apenas o numero de linhas


def gerar_matriz (n_linhas):
    return [[0]*n_linhas for x in range(n_linhas)]


# funcao de ler o arquivo recebe por parametro o nome ou caminho do msm
def ler_grafo(nome):
    comentarios = []
    properties = ""
    global num_nos
    global num_arcos
    arcos = []

    # abre um arquivo em python para leitura
    arq = open(nome, "r")

    # atribui o texto do arquivo a uma variavel
    texto = arq.read()
    # corta este texto por linhas
    texto = texto.split("\n")
    # percorre todas as linha da variavel texto
    for linha in texto:
        # se a linha iniciar com c adiciona esta a lista de comentarios
        if linha[0] == "c":
            comentarios.append(linha.replace("c ",""))
        #     se a linha iniciar com p adiciona essa as propriedades do grafo num_nos e num_arcos
        elif linha[0] == "p":
            properties=linha.replace("p edge ","")
            properties=properties.split(" ")
            num_nos = int(properties[0])
            num_arcos = int(properties[1])
            del properties;
        #  se a linha iniciar com e verifica qual a relacao e salva numa variavel que intermediará os arcos
        elif linha[0] == "e":
            linha = linha.replace("e ","")
            arcos.append(linha.split(" "))
        #     se nenhum dos quesitos for atendido fecha a aplicacao
        else:
            print ("O arquivo "+nome+" não está formatado corretamente!!!")
            exit(1)
    # fecha o arquivo
    arq.close()

    #  atribui uma matriz com o numero de linha e colunas dos nós
    grafo = gerar_matriz(num_nos)

    # percorres todos os arcos e converte de string para inteiro
    for arc in arcos:
        for i in range(2):
            arc[i] = int(arc[i])

    # printa todos os comentarios
    print ("----------------------------------------------\nComentarios:")

    for comentario in comentarios:
        print(comentario)

    # percorre todos os arcos e atribui 1  nas suas posicoes de raalacao
    for arc in arcos:
        grafo[arc[0]-1][arc[1]-1] = 1

    #  printa cada linha de representacao do grafo
    for i in range(num_nos):
        print(grafo[i])

    # retorna o grafo lido(depois vou remover os prints blz?)
    return grafo


# verifica quais são so nós fontes e sorvedouros
def source_and_sink():
    global num_nos,grafo,source
    indice=0;
    for i in range(num_nos):
        for j in range(num_nos):
            if grafo[i][j] == 1 & grafo[j][i] == 0 & i != j:
                if not i in source:
                    source.append(i)
            elif grafo[j][i] == 1 & grafo[i][j] == 0 & j != i:
                if not j in sink:
                    sink.append(j)


def main():
    global grafo,fonte
    # try:
    grafo=ler_grafo("grafo.txt")
    print("Número de nós:"+str(num_nos))
    print("Número de arcos:"+str(num_arcos))
    source_and_sink()
    for nos in source:
        print(str(nos+1)+" é um nó fonte\n")
    for nos in sink:
        print(str(nos+1)+" é um nó sorvedouro\n")
    # except:
    # print("Erro ao abrir arquivo")

main()
