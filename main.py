# encoding: utf-8
import sys
import random
from copy import deepcopy
from datetime import datetime
num_nos = 0
num_arcos = 0
grafo = ""
arcos = []
nome=""
# lista de nos font/e
source = []
#lista de graus de cada no fonte
graus = []
# lista de nos que consigo alcançar a partir de cada fonte
alcancaveis = []
# lista de nos alcançados nos algoritmos
alcancados = []
# lista de posicao dos nos utilizados dente os sources para alcancar a meta
utilizados_pos = []
# lista dos nos utilizados para facilitar na exportação do dot
utilizados = []
porcentagem=60
meta=0
# funcao pra gerar matriz como a matriz é quadrada recebe apenas o numero de linhas


def gerar_matriz (n_linhas):
    return [[0]*n_linhas for x in range(n_linhas)]


# funcao de ler o arquivo recebe por parametro o nome ou caminho do msm
def ler_grafo(nome):
    comentarios = []
    properties = ""
    global num_nos
    global num_arcos
    global arcos

    # abre um arquivo em python para leitura
    arq = open(nome, "r")

    # atribui o texto do arquivo a uma variavel
    texto = arq.readlines()
    # # corta este texto por linhas
    # texto = texto.split("\n")
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
def verifica_fonte():
    i,j,soma=0,0,0
    globals()
    for j in range(num_nos):
        soma=0
        linha=0
        for i in range(num_nos):
            linha+=grafo[j][i]
            if grafo[i][j]==1:
                break
            else:
                soma+=1
        if soma==num_nos:
            source.append(j)

def salva_utilizados():
    global utilizados_pos,utilizados
    for posicao in utilizados_pos:
        utilizados.append(source[posicao])

def maior_grau():
    copia=deepcopy(graus)
    for i in range(len(utilizados_pos)):
        for j in range(len(copia)):
            if graus[utilizados_pos[i]] == copia[j]:
                copia.pop(j)
                break

    copia.sort(key=int,reverse=True)

    aux=[]

    print(copia)
    for i in range(len(graus)):
        if graus[i] == copia[0] and not i in utilizados_pos:
            aux.append(i)
    x=random.choice(aux)
    utilizados_pos.append(x)
    return x


def sorteia_no():
    copia=deepcopy(source)
    for i in range(len(utilizados_pos)):
        for j in range(len(copia)):
            if graus[utilizados_pos[i]] == copia[j]:
                copia.pop(j)
                break
    x=random.randint(0,len(copia)-1)
    while x in utilizados_pos:
        x = random.randint(0, len(copia) - 1)
    utilizados_pos.append(x)
    return x

def fecho_transitivo():
    for i in range(num_nos):
        for j in range(num_nos):
            if grafo[i][j]>=1:
                for k in range (num_nos):
                    if grafo[j][k]==1:
                        if grafo[i][k]==0:
                            grafo[i][k]=2


def verifica_alcancaveis():
    for i in range(num_nos):
        comunica=[]
        for j in range (num_nos):
            if i in source:
                if grafo[i][j]>=1:
                    comunica.append(j)
        if (len(comunica)==0)  and (i in source):
            source.remove(i)
        elif i in source:
            graus.append(len(comunica))
            alcancaveis.append(comunica)

def guloso():
    global porcentagem,alcancados,meta,utilizados_pos,alcancados
    alcancados,utilizados_pos=[],[]
    meta = (num_nos)*(porcentagem/100)
    print (meta)
    for i in range(len(source)):
        alcancados=set(alcancados).union(alcancaveis[maior_grau()])
        if len(alcancados)>=meta:
            print ("Alcançados")
            print (alcancados)
            break
        elif (len(utilizados_pos)==len(source)) and len(alcancados)<meta:
            print ("Não foi possivel cobrir o grafo")
            break



def aleatorio():
    global porcentagem,meta,utilizados_pos,alcancados
    alcancados,utilizados_pos=[],[]
    meta = (num_nos)*(porcentagem/100)
    for i in range(len(source)):
        alcancados = set(alcancados).union(alcancaveis[sorteia_no()])
        if len(alcancados) >= meta:
            print ("Alcançados")
            print (alcancados)
            break
        elif (len(utilizados_pos) == len(source)) and len(alcancados) < meta:
            print ("Não foi possivel cobrir o grafo")
            break

def export_dot(nome_dot):
    nos=[]

    for i in range(num_nos):
        nos.append(i)
        
    # for alcancavel in alcancaveis:
    #     nos=set(nos).difference(alcancavel)
    arq = open(nome_dot+".dot","w")

    salva_utilizados()
    print (source)
    print (utilizados)


    arq.write("digraph\n{\n")
    for no in nos:
        if no in source:
            arq.write("\t"+str(no+1)+" [fillcolor=yellow, style=filled];\n")
        elif no in alcancados:
            arq.write("\t"+str(no+1)+" [color=red];\n")
        elif not no in source and not no in alcancados:
            arq.write("\t"+str(no+1)+" [color=black];\n")

    for i in range(num_nos):
        for j in range(num_nos):
            if grafo[i][j]>=1:
                if j in alcancados and i in utilizados:
                    arq.write("\t"+str(i+1)+" -> "+str(j+1)+" [color=red];\n")
                else:
                    arq.write("\t"+str(i+1)+" -> "+str(j+1)+";\n")

    # for arco in arcos:
    #     arq.write("\t"+str(arco[0]+1)+" -> "+str(arco[1]+1)+";")
    # for fonte in source:
    #     arq.write("\t"+str(fonte+1)+" [fillcolor=yellow, style=filled];\n")

    arq.write("}")
    arq.close()



def main():
    random.seed(datetime.now())
    global grafo,source,alcancaveis,graus,nome
    nome="vc1"
    # try:
    grafo=ler_grafo(nome+".txt")
    print("Número de nós:"+str(num_nos))
    print("Número de arcos:"+str(num_arcos))
    verifica_fonte()
    fecho_transitivo()
    verifica_alcancaveis()
    print("Nós fonte:")
    print (source)
    print ("Graus:")
    print (graus)
    print ("Comunicam:")
    print (alcancaveis)
    # guloso()
    aleatorio()
    export_dot(nome)
    print ("-------------------------------------------------")
    #  printa cada linha de representacao do grafo
    for i in range(num_nos):
        print(grafo[i])
    print (len(alcancados))

    print (utilizados_pos)
    print (alcancados)

    # except:
    # print("Erro ao abrir arquivo")


main()
