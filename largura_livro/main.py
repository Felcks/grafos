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
inicio = entrada.rstrip(' \n')
G.read()
   

def BuscaLargura(G, s):
    cor = {}
    d = {}
    pai = {}
    for key, value in G.iteritems():
        cor[key] = 'BRANCO'
        d[key] = 999
        pai[key] = None


    cor[s] = 'CINZA'
    d[s] = 0
    fila = [s]

    while(len(fila) > 0):
        u = fila.pop(0)
        for v in G[u]:
            if(cor[v] == 'BRANCO'):
                cor[v] = 'CINZA'
                d[v] = d[u] + 1
                pai[v] = u
                fila.append(v)
        cor[u] = 'PRETO'

    
    return d


distancias = BuscaLargura(G.data, inicio)
print(distancias)
