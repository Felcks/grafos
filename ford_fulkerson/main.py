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

lista_vertice_tempo_pai = []

def BuscaProfundidade(G, u):
	
	fluxos = {}
	for key, values in G.items():

		dict_elemento_fluxo = {}
		for k, v in values.items():
			dict_elemento_fluxo[k] = 0

		fluxos[key] = dict_elemento_fluxo

	print(fluxos)
	print(G)


	cor = {}
	pai = {}
	lista = []
	#tempos = gargalo

	for key, values in G.items():
		cor[key] = 'BRANCO'
		pai[key] = None

	gargalo = 999
	GeraCaminho(G, u, gargalo, cor, lista)

	#print(tempos)
	#print(lista_vertice_tempo_pai)

def GeraCaminho(G, u, gargalo, cores, caminho):

	cores[u[0]] = 'PRETO'
	lista_vizinhos = []

	for i in G[u[0]].items():
		if(cores[i[0]] == 'BRANCO'):
			achou = False
			for l in caminho:
				if(l[0] == i[0]):
					if(i[1] > l[1]):
						lista.remove(l)
					else:
						achou = True

			if(achou == False):

				elemento_vertice_gargalo_pai = []
				elemento_vertice_gargalo_pai.append(i[0])
				elemento_vertice_gargalo_pai.append(str(int(i[1])))
				elemento_vertice_gargalo_pai.append(u[0])
				print("elemento vertice gargalo pai", elemento_vertice_gargalo_pai)
				heappush(lista_vizinhos, elemento_vertice_gargalo_pai)

	print("lista vizinhos", lista_vizinhos)

	if len(lista_vizinhos) > 0:
		
		maiorEspaco = 0		
		possivel_u = u
		pai = u
		for l in lista_vizinhos:

			if(int(l[1]) > maiorEspaco):
				maiorEspaco = int(l[1])
				possivel_u = l[0]
				print("maior espaco", maiorEspaco, l[0])
				pai = l[2]


		u = possivel_u
		if(maiorEspaco < gargalo):
			gargalo = maiorEspaco

		elemento_vertice_gargalo_pai = []
		elemento_vertice_gargalo_pai.append(u)
		elemento_vertice_gargalo_pai.append(gargalo)
		elemento_vertice_gargalo_pai.append(pai)
		heappush(caminho, elemento_vertice_gargalo_pai)
		print("oi", elemento_vertice_gargalo_pai)

		if(u != )
		GeraCaminho()
		# for l in lista:
		# 	if(l[0] == possivel_u):
		# 		lista.remove(l)
		# 		break

		# #print("escolha", u)
		# Visita(G, u, tempoMinimo, cor, tempos, lista)

def Visita(G, u, tempo, cor, tempos, lista):
    
	tempos[u[0]] = tempo
	cor[u[0]] = 'PRETO'

	for i in G[u[0]].items():
		if(cor[i[0]] == 'BRANCO'):
			achou = False
			for l in lista:
				if(l[0] == i[0]):
					print("acontece", l[0], l[1], i[0], i[1])
					if(i[1] > l[1]):
						lista.remove(l)
					else:
						achou = True

			if(achou == False):
				#print(i)
				elemento_vertice_tempo_pai = []
				elemento_vertice_tempo_pai.append(i[0])
				gargalo = tempo
				if int(i[1]) < tempo:
					gargalo = int(i[1])

				elemento_vertice_tempo_pai.append(str(gargalo))
				elemento_vertice_tempo_pai.append(u[0])
				print("elemento vertice gargalo pai", elemento_vertice_tempo_pai)
				heappush(lista, elemento_vertice_tempo_pai)

	#print("lista2", lista)
	if len(lista) > 0:
		
		tempoMinimo = 999
		possivel_u = u
		pai = u
		for l in lista:

			if(int(l[1]) < tempoMinimo):
				tempoMinimo = int(l[1])
				possivel_u = l[0]
				pai = l[2]

		u = possivel_u
		tempo = tempoMinimo
		elemento_vertice_tempo_pai = []
		elemento_vertice_tempo_pai.append(u)
		elemento_vertice_tempo_pai.append(tempo)
		elemento_vertice_tempo_pai.append(pai)
		heappush(lista_vertice_tempo_pai, elemento_vertice_tempo_pai)

		for l in lista:
			if(l[0] == possivel_u):
				lista.remove(l)
				break

		#print("escolha", u)
		Visita(G, u, tempoMinimo, cor, tempos, lista)

	# cor[u] = 'PRETO'
	# d[u] = tempo

	# tempoMinimo = 999
	# possivel_u = u
	# for key, values in G[u].items():

	# 	if(cor[key] == 'BRANCO' and int(values) < tempoMinimo):
	# 		tempoMinimo = int(values)
	# 		possivel_u = key

	# u = possivel_u
	# tempo += tempoMinimo
	# Visita(G, u, tempo, cor, d, f)

	# for v in G[u]:
	#     if(cor[v] == 'BRANCO'):
	#         tempo = Visita(G, v, tempo, cor, d, f, lista)

	# cor[u] = 'PRETO'
	# tempo = tempo + 1
	# f[u] = tempo
	# lista.insert(0, u)

BuscaProfundidade(G.data, inicio)
