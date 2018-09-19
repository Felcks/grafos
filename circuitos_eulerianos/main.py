# -*- coding: utf-8 -*-
#!/usa/bin/python3.4

#IMPLEMENTAR E TESTAR UM ALGORITMO QUE GERE UMA ORDENAÇÃO TOPOLÓGICA PARA UM DIGRAFO ACÍCLICO (DAG)

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

### dada um vertice saber o grau
def grafo_valido(Graph):
    for key, values in Graph.data.iteritems():
        if (len(values) % 2 != 0):
            return False

    return True

print(grafo_valido(G))

def quantidade_vertices(Graph):

    tam = 0
    for key, values in Graph.data.iteritems():
        tam += len(values)

    return tam/2


tam_grafo = quantidade_vertices(G)
print(tam_grafo)
lista = []
def rodar_grafo(k1, Graph):

    achou = False
    for x in Graph.data[k1]:
        
        if(lista.count(x+k1) == 0 and lista.count(k1+x) == 0):
            lista.append(k1+x)
            achou = True
            rodar_grafo(x, Graph)


    if(achou == False):
        #conferir se acabou
        if(len(lista) == tam_grafo):
            print("acabou")
        else:
            lista.pop()

rodar_grafo(entrada.rstrip(' \n'), G)
print(lista)















def profundidade(k1, Graph):

	lista.append(k1)
	distancia_i[k1] = d
	achou = False

	for x in Graph.data[k1]:
		
		if lista.count(x) >= 1 or lista_v.count(x) >= 1:
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


#p = profundidade(entrada.rstrip(' \n'), 1, )

# for key in G.data:
# 	if(key not in lista):
# 		p = profundidade(key, p, G)

# s = ""
# for x in lista:
# 	s += x 
# 	s += " "

# print(s)

# print(distancia_i)
# print(distancia_f)

