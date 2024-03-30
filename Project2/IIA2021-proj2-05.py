from jogos import *
from rastros import *

norte = [(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
este = [(8,2),(8,3),(8,4),(8,5),(8,6),(8,7)]
oeste = [(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
sul = [(2,8),(3,8),(4,8),(5,8),(6,8),(7,8)]

def inQuadOrGoodPosition(estado,jogador):
    if (jogador == "S"):
        if (estado.white[0] > 4 and estado.white[1] < 5):
            if (estado.white[0] > 6 and estado.white[1] < 3):
                return 7
            return 6
        if ((estado.white in sul) or (estado.white in oeste)):
            return 4
    if (jogador == "N"):
        if (estado.white[0] < 5 and estado.white[1] > 4):
            if (estado.white[0] < 3 and estado.white[1] > 6):
                return -7
            return -6
        if ((estado.white in norte) or (estado.white in este)):
            return -4
    return 0

def heuristica(estado,jogador):
    if estado.terminou == 1:
        return 10 if jogador == "S" else -10
    elif estado.terminou == -1:
        return 10 if jogador == "N" else -10
    else:
        distancia1 = (distancia(estado.white,(1,8)) - distancia(estado.white,(8,1)))
        distancia2 = (distancia(estado.white,(8,1)) - distancia(estado.white,(1,8)))
        return (distancia1*0.7 + inQuadOrGoodPosition(estado,jogador)*0.5) if jogador == "S" else (
                -distancia2*0.7 + inQuadOrGoodPosition(estado,jogador)*0.5)

panda = Jogador("Panda",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,depth_for_all,eval_fn=heuristica))

todosJog.append(panda)

faz_campeonato(todosJog)