# -*- coding: utf-8 -*-
import os
import sys
from heapq import heappush, heappop

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

            di = {}
            i = 0
            v = ''
            for a in neighbours:
            	if(i == 0):
            		v = a
            		i += 1
            	else:
            		di[v] = a
            		i = 0


            data[u] = di #neighbours
        
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

lista_vertice_tempo_pai = []
#print(G.data)


def BuscaProfundidade(G, u):

	cor = {}
	pai = {}
	tempos = {}
	lista = []

	for key, values in G.items():
		cor[key] = 'BRANCO'
		pai[key] = None

	tempo = 0

	tempo = Visita(G, u, tempo, cor, tempos, lista)
	print("possibilidades :" , tempo)

	#print(tempos)
	#print(lista_vertice_tempo_pai)


def Visita(G, u, tempo, cor, tempos, lista):
    
	tempos[u[0]] = tempo
	cor[u[0]] = 'PRETO'
	lista = []

	for i in G[u[0]].items():
		if(cor[i[0]] == 'BRANCO'):
			achou = False
			for l in lista:
				if(l[0] == i[0]):
					print("acontece", l[0], l[1], i[0], i[1])
					if(i[1] < l[1]):
						lista.remove(l)
					else:
						achou = True

			if(achou == False):
				#print(i)
				elemento_vertice_tempo_pai = []
				elemento_vertice_tempo_pai.append(i[0])
				elemento_vertice_tempo_pai.append(str(int(i[1]) + tempo))
				elemento_vertice_tempo_pai.append(u[0])
				heappush(lista, elemento_vertice_tempo_pai)

	if len(lista) > 0:
		
		tempoMinimo = 999
		possivel_u = u
		pai = u
		for l in lista:
			tempo = Visita(G, l[0], tempo, cor, tempos, lista)
			for y in lista:
				cor[y[0]] = 'BRANCO'	

		return tempo	
	else:
		tempo += 1
		return tempo







BuscaProfundidade(G.data, 'A')
# BuscaProfundidade(G.data, 'B')
# BuscaProfundidade(G.data, 'C')
# BuscaProfundidade(G.data, 'D')
# BuscaProfundidade(G.data, 'E')
# BuscaProfundidade(G.data, 'F')
# BuscaProfundidade(G.data, 'G')
