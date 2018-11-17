# encoding: utf-8

# funcao pra gerar matriz como a matriz é quadrada recebe apenas o numero de linhas
def gerar_matriz (n_linhas):
    return [[0]*n_linhas for x in range(n_linhas)]


#funcao de ler o arquivo recebe por parametro o nome ou caminho do msm
def ler_arquivo(nome):
    comentario = []
    i = 0
    j = 0
    properties = ""
    num_nos = 0
    num_arcos = 0
    intermedia_arcos = []
    arcos = []

    # abre um arquivo em python para leitura
    arq = open(nome, "r")

    # atribui o texto do arquivo a uma variavel
    texto = arq.read()
    # corta este texto por linhas
    texto = texto.split("\n");
    # percorre todas as linha da variavel texto
    for linha in texto:
        # se a linha iniciar com c adiciona esta a lista de comentarios
        if linha[0] == "c":
            comentario.append(linha.split("c "))
        #     se a linha iniciar com p adiciona essa as propriedades do grafo num_nos e num_arcos
        elif linha[0] == "p":
            properties=linha.split("p edge ")
            properties=properties[1].split(" ")
            num_nos = int(properties[0])
            num_arcos = int(properties[0])
        #  se a linha iniciar com e verifica qual a relacao e salva numa variavel que intermediará os arcos
        elif linha[0]=="e":
            intermedia_arcos.append(linha.split("e "))
        #     se nenhum dos quesitos for atendido fecha a aplicacao
        else:
            print "O arquivo "+nome+" não está formatado corretamente!!!"
            exit(1)
    # fecha o arquivo
    arq.close()

    #  atribui uma matriz com o numero de linha e colunas dos nós
    grafo=gerar_matriz(num_nos)

    # remove os comentarios vazios pois não consegui de outra forma "famosa gambiarra"
    for c in comentario:
        c.pop(0)

    # separa os arcos de uma maneira mais organizada e adiciona a variavel arcos
    for a in intermedia_arcos:
        a.pop(0)
        for x in a:
            arcos.append(x.split(" "))

    # deleta a variavel que intermediava os arcos
    del intermedia_arcos

    # percorres todos os arcos e converte de string para inteiro
    for arc in arcos:
        for i in range(2):
            arc[i] = int(arc[i])

    # printa todos os comentarios
    print ("----------------------------------------------\nComentarios:")

    for c in comentario:
        for x in c:
            print(x)

    # printa o numero de nos e de arcos
    print ("----------------------------------------------\nNúmero de Nós:"+str(num_nos)+"\nNúmero de Relacões:"+str(num_arcos)+"\n----------------------------------------------\nRelacoes")

    # percorre todos os arcos e atribui 1  nas suas posicoes de raalacao
    for arc in arcos:
        grafo[arc[0]][arc[1]] = 1

    #  printa cada linha de representacao do grafo
    for i in range(num_nos):
        print grafo[i]

    # retorna o grafo lido(depois vou remover os prints blz?)
    return grafo


def main():
    try:
        grafo=ler_arquivo("grafo.txt")
    except:
        print "Erro ao abrir arquivo"

main()
