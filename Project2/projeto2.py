from jogos import *
from rastros import *


hotspot = [(3,3),(4,3),(5,3),(6,3),(6,4),(6,5),(6,6),
           (5,6),(4,6),(3,6),(3,5),(3,4)]

vitoriaS = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
            (2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)]

vitoriaN = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),
            (8,2),(8,3),(4,8),(5,8),(6,8),(7,8),(8,8)]

def algoritmo(estado,jogador) :
    casasPerde = [(7,1),(7,2),(8,2)]
    casasVitoria = [(1,7),(2,7),(2,8)]
    casasOndePodesIr = estado.moves()
    
    if (estado.white == (2,2)) & ((1,1) in casasOndePodesIr):
        return 3
    
    if (estado.white == (7,7)) & ((8,8) in casasOndePodesIr):
        return 3
    
    if estado.white in vitoriaS:
        for i in casasOndePodesIr:
            if i in vitoriaS:
                return distancia((1,8), i)
    
    for i in casasOndePodesIr:
        if (jogador == "S") & (i == (1,8)):
            return 0
        if i in hotspot:
            return 2
        if i in casasPerde:
            return 7
        if i in casasVitoria:
            return 1
        if jogador == "S":
            for j in vitoriaS:
                if ((estado.white[0] == j[0]) & (
                        estado.white[1] != j[1])
                        ) | ((estado.white[1] == j[1]
                        ) & (estado.white[0] != i[0])
                        ) & (j in casasOndePodesIr):
                    return 2
                

def distancia (a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def heuristica(estado,jogador):
    if estado.terminou == 1:
        return 10 if jogador == "S" else -10
    elif estado.terminou == -1:
        return 10 if jogador == "N" else -10
    else:
        return 7-algoritmo(estado.white,jogador)

nosso = Jogador("Nosso",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,5,eval_fn=heuristica))

todosJog.append(nosso)