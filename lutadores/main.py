# -*- coding: utf-8 -*-
#!/usa/bin/python3.4

import os
import sys

class Graph:
    
    def __init__(self):

        self.data = {}

    def read(self,filename=None,ignore=0):
        
        if filename:
           f = open(filename)
        else:   
           f = sys.stdin
        
        while ignore>0: # ignora linhas iniciais do problema para ler somente o grafo
            f.readline()
            ignore -= 1
        
        data = {}
        for line in f:
            v_list     = line.split()
            u          = v_list[0]
            neighbours = v_list[1:] 
            data[u]       = neighbours
            #print(data)
        
        self.data = data    
        
        return data
    
    def add_edge(self,u,v): # para fazer em memória
        
        try:
            self.data[u].append(v)
        except:
            self.data[u] = [v]
        
    def add_neighbours(self,u,n_list):
        
        try:
            self.data[u] += n_list
        except:
            self.data[u] = n_list
    
    def check(self): # garante que não hajam vértices repetidos

        data = self.data
        for v in data:
            data[v] = list(set(data[v]))

    def __str__(self):

        s = "############# Graph ###############\n"
        s+= str(self.data)
        s+= "###################################\n"        
        return s

        

# cria o objeto grafo
G = Graph()

### Carga via entrada de dados (arquivo ou entrada padrão) ###
f = sys.stdin
entrada = f.readline()
G.read()


##lado igual a true ou false
lista = []
lista2 = []

lista.append(entrada.rstrip(' \n'))
lista2.append(True)

def largura(Graph):

    index = 0;
    profundidade = True;
    while(index < len(lista)):

        if(index > 0):
            if(lista2[index] != lista2[index-1]):
                profundidade = not profundidade
        elif(index == 0):
                profundidade = not profundidade

        k1 = lista[index]
        for x in Graph.data[k1]:
            
            if lista.count(x) >= 1:

                for i in range(0, len(lista)):
                    if(lista[i] == x):
                        if(lista2[i] != profundidade):
                            print("esse grafo nao'serve")
                            return
                #aqui eu tenho que conferir se ele existe na lista
                #se existir tenho que ver se a profundidade que eu vou dar pra ele vai ser igual a que ele tem de fato
                pass
            else:
                lista.append(x)
                lista2.append(profundidade)
                        

        index += 1

    return False

largura(G)

#Removendo o A e a distancia para A
#lista.pop(0)
#lista2.pop(0)

data = {}
i = 0
while(i < len(lista)):
    data[lista[i]] = lista2[i]
    i += 1

ordenado = data.keys()
ordenado.sort()

s = ""
for x in ordenado:
    s += x + " " + str(data[x])
    print(s)
    s = ""

