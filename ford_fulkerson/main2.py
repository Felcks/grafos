# -*- coding: utf-8 -*-
import os
import sys
from heapq import heappush, heappop

''' ENTRADAS SENDO USADAS PELO ALGORITMO !!!
S
S A 16 C 13 
A B 12 C 10 S 0
B C 9 T 20 D 0 A 0
C A 4 D 14 S 0 B 0
D B 7 T 4 C 0
T B 0 D 0
'''


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

def Ford_Fulkerson(G, u):
	
	## Iniciando todos os fluxos com 0
	fluxos = {}
	for key, values in G.items():

		dict_elemento_fluxo = {}
		for k, v in values.items():
			dict_elemento_fluxo[k] = 0

		fluxos[key] = dict_elemento_fluxo

	cor = {}
	lista = []

	## Loop que vai rodar até achar exister um caminho aumentate
	gargalo = 999
	while(True):
		lista = []
		for key, values in G.items():
			cor[key] = 'BRANCO'
		
		gargalo = GeraCaminho(G, u, gargalo, cor, lista, fluxos)
		if gargalo != 999:
			AumentaFluxo(G, fluxos, lista, gargalo)
		else:
			break


	## Adicionando o fluxo de chegada a uma variável
	fluxo_chegada_final = 0
	for key, value in fluxos.items():
		if key == 'T':
			for k, v in value.items():
				fluxo_chegada_final += v

			break


	## Prints final
	print("")
	print("Grafo de Fluxos:")
	print(fluxos)
	print("Fluxo final de chegada:", -fluxo_chegada_final)


def AumentaFluxo(G, fluxos, caminho, gargalo):
	
	for c in caminho:
		pai = c[2]
		filho = c[0]

		fluxos[pai][filho] += gargalo
		fluxos[filho][pai] -= gargalo


def GeraCaminho(G, u, gargalo, cores, caminho, fluxos):

	cores[u[0]] = 'PRETO'
	lista_vizinhos = []

	## Adiciona todos os vizinhos que não estão pintados para lista de possivel vizinho
	for i in G[u[0]].items():
		if(cores[i[0]] == 'BRANCO'):
			achou = False
			for l in caminho:
				if(l[0] == i[0]):
					if(i[1] > l[1]):
						lista_vizinhos.remove(l)
					else:
						achou = True

			if(achou == False):

				# Vertice-gargalo-pai ex: {u, 12, v}
				elemento_vertice_gargalo_pai = []
				elemento_vertice_gargalo_pai.append(i[0])
				
				# Momento que calcula a capacidade residual
				capacidade_maxima = int(i[1])
				fluxo_atual = fluxos[i[0]][u[0]]

				capacidade_real = capacidade_maxima + fluxo_atual
				if capacidade_real > capacidade_maxima:
					capacidade_real = capacidade_maxima
				elemento_vertice_gargalo_pai.append(str(capacidade_real))
				
				# Adicionando ao pai e colocando na lista de vizinhos
				elemento_vertice_gargalo_pai.append(u[0])
				heappush(lista_vizinhos, elemento_vertice_gargalo_pai)



	## Escolhendo o melhor vizinho para ir - Aquele com maior gargalo
	if len(lista_vizinhos) > 0:
		
		maiorEspaco = 0		
		possivel_u = u
		pai = u
		achou_espaco_vazio = False

		for l in lista_vizinhos:

			if(int(l[1]) > maiorEspaco):
				maiorEspaco = int(l[1])
				possivel_u = l[0]
				pai = l[2]
				achou_espaco_vazio = True

		if achou_espaco_vazio == False:
			return 999

		# Se o maior vizinho for o novo gargalo - fazemos a troca
		if(maiorEspaco < gargalo):
			gargalo = maiorEspaco

		u = possivel_u
		elemento_vertice_gargalo_pai = []
		elemento_vertice_gargalo_pai.append(u)
		elemento_vertice_gargalo_pai.append(gargalo)
		elemento_vertice_gargalo_pai.append(pai)
		heappush(caminho, elemento_vertice_gargalo_pai)
		

		if(u != 'T'):
			gargalo = GeraCaminho(G, u, gargalo, cores, caminho, fluxos)
		
		return gargalo


Ford_Fulkerson(G.data, inicio)