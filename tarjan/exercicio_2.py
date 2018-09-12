# -*- coding: utf-8 -*-
#!/usa/bin/python3.4

#IMPLEMENTAR O ALGORITMO DE TARJAN PARA IDENTIFICAR PONTES EM UM GRAFO
#SEU ALGORITMO DEVE INFORMAR ARESTAS DO TIPO PONTE

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

lista = [] #chaves
lista_v = [] #chaves adicionadas
distancia_i = {} #distancias iniciais
distancia_f = {} #distancias finais

def profundidade(k1, d, Graph):

	lista.append(k1)
	distancia_i[k1] = d
	achou = False

	for x in Graph.data[k1]:
		
		if lista.count(x) >= 1:
			#distancias_i
			pass
		# elif x == k2:
		# 	lista.append(k2)
		# 	return True
		else:
			if(achou == True):
				d = profundidade(x,d, Graph) #6
			else:
				d = profundidade(x,d+1, Graph)
			achou = True
	
	distancia_f[k1] = d

	if(achou == False):
		d = d+1
		distancia_f[k1] = d

	#lista.pop()
	return d+1


p = profundidade(entrada.rstrip(' \n'), 1, G)
for key in G.data:
	if(key not in lista):
		p = profundidade(key, p, G)


print(distancia_i)
print(distancia_f)