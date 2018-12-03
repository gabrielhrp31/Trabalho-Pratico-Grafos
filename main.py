# encoding: utf-8
import sys
from copy import deepcopy
num_nos = 0
num_arcos = 0
grafo = ""
source = []
graus = []
influenciados = []
utilizados = []
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

    # retorna o grafo lido(depois vou remover os prints blz?)
    return grafo


# verifica quais são so nós fontes e sorvedouros
def fonte_grau():
    globals()
    for i in range(num_nos):
        comunica=[]
        soma=0
        for j in range(num_nos):
            soma+=grafo[i][j]
            if grafo[i][j]==1:
                comunica.append(j)
            if j == num_nos-1:
                if soma>0 :
                    source.append(i)
                    graus.append(soma)
                    influenciados.append(comunica)
    print(influenciados)
    del comunica
    del soma


def maior_grau():
    copia=deepcopy(graus)
    for i in range(len(utilizados)):
        for j in range(len(copia)):
            if graus[utilizados[i]] == copia[j]:
                copia.pop(j)
                break
    copia.sort(key=int,reverse=True)
    print(copia)

    for i in range(len(graus)):
        if graus[i] == copia[0]:
            utilizados.append(i)
            return i

def guloso():
    print("calcula o algoritmo guloso")


def fecho_transitivo():
    for i in range(num_nos):
        for j in range(num_nos):
            if grafo[i][j]>=1:
                for k in range (num_nos):
                    if grafo[j][k]==1:
                        if grafo[i][k]==0:
                            grafo[i][k]=2
def randomico():
    print("calcula o algoritmo randomico")

def main():
    global grafo,source
    # try:
    grafo=ler_grafo("grafo3.txt")
    print("Número de nós:"+str(num_nos))
    print("Número de arcos:"+str(num_arcos))
    fonte_grau()
    fecho_transitivo()
    print("Nós fonte:")
    for i in range(len(source)):
        print("O nó "+str(source[i]+1)+" é fonte  e tem grau "+str(graus[i]))
    #  printa cada linha de representacao do grafo
    for i in range(num_nos):
        print(grafo[i])
    # except:
    # print("Erro ao abrir arquivo")

main()
