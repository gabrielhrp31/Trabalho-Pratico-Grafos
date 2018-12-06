# encoding: utf-8
import sys
import random
from copy import deepcopy
import time
import timeit
from datetime import datetime
semente=0
metodo="a"
num_nos = 0
num_arcos = 0
grafo = ""
arcos = []
nome=""
nome_saida=""
# lista de nos fonte
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
porcentagem=0
meta=0
# funcao pra gerar matriz como a matriz é quadrada recebe apenas o numero de linhas


def gerar_matriz (n_linhas):
    return [[0]*n_linhas for x in range(n_linhas)]


# funcao de ler o arquivo recebe por parametro o nome ou caminho do msm
def ler_grafo():
    global nome
    comentarios = []
    properties = ""
    global num_nos
    global num_arcos
    global arcos

    # abre um arquivo em python para leitura
# try:
    arq = open(nome, "r")
    # atribui o texto do arquivo a uma variavel
    texto = arq.readlines()
    # # corta este texto por linhas
    # texto = texto.split("\n")
    # percorre todas as linha da variavel texto
    for linha in texto:
        # se a linha iniciar com c adiciona esta a lista de comentarios
        if linha[0] == "c":
            comentarios.append(linha.replace("c ", ""))
        #     se a linha iniciar com p adiciona essa as propriedades do grafo num_nos e num_arcos
        elif linha[0] == "p":
            properties = linha.replace("p edge ", "")
            properties = properties.split(" ")
            num_nos = int(properties[0])
            num_arcos = int(properties[1])
            del properties;
        #  se a linha iniciar com e verifica qual a relacao e salva numa variavel que intermediará os arcos
        elif linha[0] == "e":
            linha = linha.replace("e ", "")
            arcos.append(linha.split(" "))
        #     se nenhum dos quesitos for atendido fecha a aplicacao
        else:
            print ("O arquivo " + nome + " não está formatado corretamente!!!")
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
        grafo[arc[0] - 1][arc[1] - 1] = 1

    # retorna o grafo lido(depois vou remover os prints blz?)
    return grafo
# except:
    print ("O arquivo "+nome+" não existe")




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
    meta = (num_nos)*(porcentagem/100.0)
    for i in range(len(source)):
        alcancados=set(alcancados).union(alcancaveis[maior_grau()])
        if len(alcancados)>=meta:
            print (str(porcentagem)+"% do grafo coberta")
            break
        elif (len(utilizados_pos)==len(source)) and len(alcancados)<meta:
            print ("Não foi possivel cobrir o grafo")
            break



def aleatorio():
    global porcentagem,meta,utilizados_pos,alcancados
    alcancados,utilizados_pos=[],[]
    meta = (num_nos)*(porcentagem/100.0)
    for i in range(len(source)):
        alcancados = set(alcancados).union(alcancaveis[sorteia_no()])
        if len(alcancados) >= meta:
            print (str(porcentagem)+"% do grafo coberto")
            break
        elif (len(utilizados_pos) == len(source)) and len(alcancados) < meta:
            print ("Não foi possivel cobrir o grafo")
            break

def export_dot():

    nos=[]
    global nome_saida

    for i in range(num_nos):
        nos.append(i)

    arq = open("dot/"+nome_saida+".dot","w")

    salva_utilizados()


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
    arq.write("}")
    arq.close()

# Exportação .log

def export_log():
    global nome_saida,semente,metodo,utilizados,nome
    nos = []

    try:
        arq = open("log/"+nome_saida+".log", 'r')
        arq.close()
    except IOError:
        arq = open("log/"+nome_saida+".log", 'w')
        arq.write("INSTANCE \t\t\t\t NODES \t\t SEED \t\t METHOD \t DSIZE \n")
        arq.close()

    arq = open("log/"+nome_saida+".log", 'a+')

    arq.write(nome+" \t\t "+str(num_nos)+" \t\t " +str(semente)+ " \t\t "+metodo+" \t\t\t "+str(len(utilizados))+"\n")
    arq.close()

def export_tempo(tempo):
    nome_csv=nome.replace(".txt","-"+metodo+".CSV")
    arq=open("CSV/"+nome_csv,"a+")
    arq.write(str(tempo)+";\n")



def main():
    global semente,grafo,source,alcancaveis,graus,nome,metodo,nome_saida,porcentagem
    inicio = timeit.default_timer()
    semente=sys.argv[1]
    porcentagem=sys.argv[2]
    porcentagem=int(porcentagem)
    metodo=sys.argv[3]
    nome=sys.argv[4]
    nome_saida=sys.argv[5]
    random.seed(semente)
    grafo=ler_grafo()
    verifica_fonte()
    fecho_transitivo()
    verifica_alcancaveis()
    if metodo == "g":
        guloso()
    elif metodo == "a":
        aleatorio()
    export_dot()
    export_log()
    fim = timeit.default_timer()
    print ("Tempo de execução: ",round(fim-inicio,2))
    export_tempo(round(fim-inicio,2))

main()
