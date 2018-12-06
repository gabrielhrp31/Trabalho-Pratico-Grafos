# encoding: utf-8
import sys
import random
from copy import deepcopy
num_nos = 0
num_arcos = 0
grafo = ""
arcos = []
nome=""
source = []
graus = []
alcancaveis = []
alcancados = []
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
    for j in range(num_nos): # De 1 ate numero de nos
        soma=0
        linha=0
        for i in range(num_nos): # De 1 ate numero de nos
            linha+=grafo[j][i] # linha recebe o valor dela + grafo
            if grafo[i][j]==1: # Se grafo for igual a 1
                break # Mata o programa
            else: # Se não
                soma+=1 # soma recebe soma + 1
        if soma==num_nos: # Se soma for igual a numero de nos
            source.append(j) # source acrescenta j


# Função para achar o maior grau --??--

def maior_grau():
    copia=deepcopy(graus) # Cria uma cópia de graus
    for i in range(len(utilizados)): # De 1 ate utilizados
        for j in range(len(copia)): # De 1 ate copia
            if graus[utilizados[i]] == copia[j]: # Se graus utilizados na posição i for igual a copia na posição j
                copia.pop(j) # copia irá apagar o j
                break # Mata o programa
    copia.sort(key=int,reverse=True) # --??--

    print(copia)

    for i in range(len(graus)): # De 1 ate graus
        if graus[i] == copia[0]: # Se graus for igual a copia na posição 0
            utilizados.append(i) # utilizados acrescenta i
            return i # Retorna o valor de i


# Função para sortear um no --??--

def sorteia_no():
    copia=deepcopy(source) # Cria uma cópia de source
    for i in range(len(utilizados)): # De 1 ate utilizados
        for j in range(len(copia)): # De 1 ate copia
            if graus[utilizados[i]] == copia[j]: # Se graus utilizados na posição i for igual a copia na posição j
                copia.pop(j) # copia irá apagar o j
                break
    x=random.randint(0,len(copia)-1) # x faz --??--
    utilizados.append(x) # utilizados acrescenta x
    return x # Retorna o valor de x


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
        if i in source:
            graus.append(len(comunica)) # graus acrescenta comunica
            alcancaveis.append(comunica) # alcancaveis acrescenta comunica

# Função gulosa

def guloso():
    global porcentagem,alcancados,meta,utilizados,alcancados
    alcancados,utilizados=[],[]
    meta = (num_nos)*(porcentagem/100) # Meta a ser atingida em %
    print (meta)
    for i in range(len(source)):  # Roda de 1 ate o tamanho dos source
        alcancados=set(alcancados).union(alcancaveis[maior_grau()]) # alcancados = união entre alcancados com o maior grau de alcancados
        if len(alcancados)>=meta: # Se alcancados for maior ou igual a meta
            print ("Alcançados")
            print (alcancados)
            break
        elif (len(utilizados)==len(source)) and len(alcancados)<meta: # Se não, se alcancados = source ou menor que a meta
            print ("Não foi possivel cobrir o grafo")
            break



# Função aleatoria

def aleatorio():
    global porcentagem,meta,utilizados,alcancados
    alcancados,utilizados=[],[]
    meta = (num_nos)*(porcentagem/100) # Meta a ser atingida em %
    for i in range(len(source)): # Roda de 1 ate o tamanho dos source
        alcancados = set(alcancados).union(alcancaveis[sorteia_no()]) # alcancados = união entre alcancados com o no sorteado
        if len(alcancados) >= meta: # Se alcancados for maior que a meta
            print ("Alcançados")
            print (alcancados)
            break
        elif (len(utilizados) == len(source)) and len(alcancados) < meta: # Se não, se os utilizados for = aos source e menor que meta
            print ("Não foi possivel cobrir o grafo")
            break

# Exportação do .dot

def export_dot():
    global nome
    nos=[]

    for i in range(num_nos-1): # roda de 1 ate o n° de nos - 1
        nos.append(i) # adiciona no na posição i
    set(nos).difference(source) # união entre os nos
    for alcancavel in alcancaveis:
        set(nos).difference(alcancavel) # união entre nos e alcancaveis

    arq = open(nome+".dot","w")


    arq.write("digraph\n{\n")
    for no in nos:
        arq.write("\t"+str(no+1)+" [color=black];\n")
    for fonte in source:
        arq.write("\t"+str(fonte+1)+" [fillcolor=yellow, style=filled];\n")
    for alcancavel in alcancaveis:
        for no in alcancavel:
            arq.write("\t"+str(no+1)+" [color=red];\n")
    for arco in arcos:
        arq.write("\t"+str(arco[0])+" -> "+str(arco[1])+" [color=black];\n")
    for i in range(len(source)):
        for alcancavel in alcancaveis[i]:
            arq.write("\t"+str(source[i]+1)+" -> "+str(alcancavel)+" [color=red];\n")
    arq.write("}");
    arq.close()


#Main
def main():
    global grafo,source,alcancaveis,graus,nome
    nome="vc1"
    # try:
    grafo=ler_grafo(nome+".txt")
    print("Número de nós:"+str(num_nos))
    print("Número de arcos:"+str(num_arcos))
    verifica_fonte() # Chamada da função para verificar os nos fontes
    fecho_transitivo() # Chamada da função para achar os fechos transitivos
    verifica_alcancaveis() # Chamada da função para verificar os nos alcançaveis
    export_dot() # Exportação para o .dot
    print("Nós fonte:")
    print (source)
    print ("Graus:")
    print (graus)
    print ("Comunicam:")
    print (alcancaveis)
    # guloso() # Função gulosa  para gerar o grafo
    aleatorio() # Função aleatoria para gerar o grafo
    print ("-------------------------------------------------")
    #  printa cada linha de representacao do grafo
    for i in range(num_nos):
        print(grafo[i])
    print (len(alcancados))
    # except:
    # print("Erro ao abrir arquivo")


main()
