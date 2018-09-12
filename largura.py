# -*- coding: utf-8 -*-
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

lista = []
lista2 = []

lista_v = {}
lista_v[entrada.rstrip(' \n')] = 0

#lista.append(entrada.rstrip(' \n'))
#lista2.append(0)

def caminhoMinimo(Graph):

    index = 0;
    profundidade = 1;
    oldValue = 'A'
    for key, value in lista_v.iteritems():

        if(index > 0):
            if(value != oldValue):
                profundidade += 1

        for x in Graph.data[key]:
            
            if x in lista_v:
                pass
            else:
                lista_v[x] = profundidade
                        

        index += 1



    return False

caminhoMinimo(G)
print(lista_v)

# A B D
# B A C D
# C B
# D A B

v --> A { A}

#Removendo o A e a distancia para A
#lista.pop(0)
#lista2.pop(0)




s = ""
for i in range(0, len(lista)):
    s += entrada.rstrip(' \n') + " " + lista[i] + " " + str(lista2[i])
    print(s)
    s = ""