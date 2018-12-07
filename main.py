# encoding: utf-8

##------------------------------
##
## Gabriel Henrique - 0040892
## Lucas Oliveira - 0040498
## Tiago Rodrigues - 0041191
##
## Foi utilizado o PyCharm como ambiente de trabalho, junto com o Phyton 3. Ao tempo de execução, foram gastos cerca de 3 dias para fazer tudo.
## Existe uma função para cada parte do trabalho, onde todas estão sob o main e com comentarios de referências e comentarios explicando cada linha.
## As compilações foram todas embazadas no requisito do trabalho. python main.py <semente> <p-difusao> <metodo> <nome_entrada> <nome_saida>
## Foi utilizado uma máquina com processador i5 8ªG(8 GB ram) e um i5 7ªG (4 GB ram)
##
##
##------------------------------------------------------------------------------------

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
    for j in range(num_nos): # De 1 ate numero de nos
        soma=0
        linha=0
        for i in range(num_nos): # De 1 ate numero de nos
            linha+=grafo[j][i] # linha recebe o valor dela + grafo
            if grafo[i][j]==1: # Se grafo for igual a 1
                break # Mata o programa
            else: # Senão
                soma+=1 # soma recebe soma + 1
        if soma==num_nos: # Se soma for igual a numero de nos
            source.append(j) # source acrescenta j


# salva os laços utilizados
def salva_utilizados():
    global utilizados_pos,utilizados
    for posicao in utilizados_pos: # De posicao ate posicao de utilizados
        utilizados.append(source[posicao]) # utilizados acrescenta posicao do source


# Função para achar o maior grau
def maior_grau():
    copia=deepcopy(graus) # Cria uma cópia de graus
    for i in range(len(utilizados)): # De 1 ate utilizados
        for j in range(len(copia)): # De 1 ate copia
            if graus[utilizados[i]] == copia[j]: # Se graus utilizados na posição i for igual a copia na posição j
                copia.pop(j) # copia irá apagar o j
                break # Mata o programa

    copia.sort(key=int,reverse=True)

    aux=[]

    for i in range(len(graus)): # De 1 ate graus
        if graus[i] == copia[0] and not i in utilizados_pos: # Se graus for igual a copia na posição 0 e não for a posição utilizada
            aux.append(i) # aux acrescenta i
    x=random.choice(aux) # x escolhe um aux aleatório
    utilizados_pos.append(x) # posição utilizados acrescenta i
    return x # Retorna o valor de x


# Função para sortear um no
def sorteia_no():
    copia=deepcopy(source) # Cria uma cópia de source
    for i in range(len(utilizados)): # De 1 ate utilizados
        for j in range(len(copia)): # De 1 ate copia
            if graus[utilizados[i]] == copia[j]: # Se graus utilizados na posição i for igual a copia na posição j
                copia.pop(j) # copia irá apagar o j
                break # Mata o programa
    x=random.randint(0,len(copia)-1) # x pega um aleatório de copia - 1
    while x in utilizados_pos:
        x = random.randint(0, len(copia) - 1)# x pega um aleatório de copia - 1
    utilizados_pos.append(x) # posição utilizados acrescenta x
    return x # Retorna x


# Função para achar a transitividade
def fecho_transitivo():
    for i in range(num_nos): # De 1 ate numero de nos
        for j in range(num_nos): # De 1 ate numero de nos
            if grafo[i][j]>=1:
                for k in range (num_nos): # De 1 ate numero de nos
                    if grafo[j][k]==1:
                        if grafo[i][k]==0:
                            grafo[i][k]=2
                            ## Se as posições forem as mesmas, a transitividade recebe o numero "2" para facilitar a visão


# Função de verificação de nos alcançaveis
def verifica_alcancaveis():
    for i in range(num_nos): # De 1 ate numero de nos
        comunica=[]
        for j in range (num_nos): # De 1 ate numero de nos
            if i in source: # Se i estiver em souce
                if grafo[i][j]>=1:
                    comunica.append(j) # comunica acrescenta j
        if (len(comunica)==0)  and (i in source): # Se comunica for igual a 0
            source.remove(i) # source apaga i
        elif i in source: # Senão, se
            graus.append(len(comunica)) # graus acrescenta comunica
            alcancaveis.append(comunica) # alcancaveis acrescenta comunica


# Função gulosa
def guloso():
    global porcentagem,alcancados,meta,utilizados_pos,alcancados
    alcancados,utilizados_pos=[],[]
    meta = (num_nos)*(porcentagem/100.0) # Meta a ser atingida em %
    for i in range(len(source)): # Roda de 1 ate o tamanho dos source
        alcancados=set(alcancados).union(alcancaveis[maior_grau()]) # alcancados = união entre alcancados com o maior grau de alcancados
        if len(alcancados)>=meta: # Se alcancados for maior ou igual a meta
            print (str(porcentagem)+"% do grafo coberta")
            break
        elif (len(utilizados_pos)==len(source)) and len(alcancados)<meta: # Senão, se alcancados = source ou menor que a meta
            print ("Não foi possivel cobrir o grafo")
            break


# Função aleatoria
def aleatorio():
    global porcentagem,meta,utilizados_pos,alcancados
    alcancados,utilizados_pos=[],[]
    meta = (num_nos)*(porcentagem/100.0)  # Meta a ser atingida em %
    for i in range(len(source)): # Roda de 1 ate o tamanho dos source
        alcancados = set(alcancados).union(alcancaveis[sorteia_no()]) # alcancados = união entre alcancados com o no sorteado
        if len(alcancados) >= meta: # Se alcancados for maior que a meta
            print (str(porcentagem)+"% do grafo coberto")
            break # Mata o programa
        elif (len(utilizados_pos) == len(source)) and len(alcancados) < meta: # Senão, se os utilizados for = aos source e menor que meta
            print ("Não foi possivel cobrir o grafo")
            break # Mata o programa


# Exportação do .dot
def export_dot():

    nos=[]
    global nome_saida

    for i in range(num_nos): # roda de 1 ate o n° de nos
        nos.append(i) # adiciona no na posição i

    arq = open("dot/"+nome_saida+".dot","w") # Abertura de arquivo

    salva_utilizados() # Chamada de função

    # Criação do .dot
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

    try: # Tenta abrir o arquivo
        arq = open("log/"+nome_saida+".log", 'r')
        arq.close()
    except IOError: # Se não existir
        arq = open("log/"+nome_saida+".log", 'w')
        arq.write("INSTANCE \t\t\t\t NODES \t\t SEED \t\t METHOD \t DSIZE \n")
        arq.close()

    arq = open("log/"+nome_saida+".log", 'a+')

    arq.write(nome+" \t\t "+str(num_nos)+" \t\t " +str(semente)+ " \t\t "+metodo+" \t\t\t "+str(len(utilizados))+"\n")
    arq.close()


# Exportação do tempo
def export_tempo(tempo):
    nome_csv=nome.replace(".txt","-"+metodo+".CSV")
    arq=open("CSV/"+nome_csv,"a+")
    arq.write(str(tempo)+";\n")


# Main
def main():
    global semente,grafo,source,alcancaveis,graus,nome,metodo,nome_saida,porcentagem
    inicio = timeit.default_timer()
    semente=sys.argv[1]
    porcentagem=sys.argv[2]
    porcentagem=int(porcentagem)
    metodo=sys.argv[3]
    nome=sys.argv[4]
    nome_saida=sys.argv[5]
    random.seed(semente) # Função para pegar uma semente aleatória
    grafo=ler_grafo()  # Função para ler o grafo
    verifica_fonte() # Função para verificar os fontes
    fecho_transitivo() # Função para criar os fechos transitivos
    verifica_alcancaveis() # Função para ver os alcançaveis
    if metodo == "g":
        guloso() # Função para chamar o método guloso
    elif metodo == "a":
        aleatorio() # Função para chamar o método aleatório
    export_dot() # Função para exportar o doit
    export_log() # Função para exportar o log
    fim = timeit.default_timer() # Função para o fim do tempo
    print ("Tempo de execução: ",round(fim-inicio,2))
    export_tempo(round(fim-inicio,2))

main()
