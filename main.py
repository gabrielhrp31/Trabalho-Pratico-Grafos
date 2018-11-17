def gerar_matriz (n_linhas):
    return [[0]*n_linhas for x in range(n_linhas)]


def ler_arquivo(nome):
    comentario=[]
    i = 0
    j = 0
    properties=""
    num_nos=0
    num_arcos=0
    intermedia_arcos=[]
    arcos=[]
    arq=open(nome,"r")
    texto=arq.read()
    texto=texto.split("\n");
    for linha in texto:
        if linha[0]=="c":
            comentario.append(linha.split("c "))
        elif linha[0] == "p":
            properties=linha.split("p edge ")
            properties=properties[1].split(" ")
            num_nos = int(properties[0])
            num_arcos = int(properties[0])
        elif linha[0]=="e":
            intermedia_arcos.append(linha.split("e "))
    arq.close()

    grafo=gerar_matriz(num_nos)




    for c in comentario:
        c.pop(0)
    for a in intermedia_arcos:
        a.pop(0)
        for x in a:
            arcos.append(x.split(" "))

    for arc in arcos:
        for i in range(2):
            arc[i] = int(arc[i])

    print ("\nComentarios:")

    for c in comentario:
        for x in c:
            print(x)

    print ("----------------------------------------------\nNumero de Nos:"+properties[0]+"\nNumero de Relacoes:"+properties[1]+"\n--------------------\nRelacoes")

    print arcos[1][0]
    print arcos[1][1]



    for arc in arcos:
        grafo[arc[0]][arc[1]] = 1

    print grafo



def main():
    ler_arquivo("grafo.txt")


main()