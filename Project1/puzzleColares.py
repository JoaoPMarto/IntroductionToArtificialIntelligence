from searchPlus import *
import sys

class PuzzleCores:
    
    x = ["blue","green","green","green","green","green","green","green","green",
         "green","green","red","red","red","red","red","red","red","red","red"]
    y = ["blue","blue","blue","blue","green","cyan","cyan","cyan","cyan","cyan",
         "cyan","cyan","cyan","cyan","blue","blue","blue","blue","blue","blue"]

    def __init__(self, colar1 = x, colar2 = y):
        
        self.colar1 = colar1
        self.colar2 = colar2
    
    def getColar1(self) :
        return self.colar1.copy()
    
    def getColar2(self) :
        return self.colar2.copy()
    
    def rodarDireita(self,colar):
        x = colar[len(colar)-1]
        i = len(colar)-1
        while i > 0:
            colar[i] = colar[i-1]
            i -= 1
        colar[0] = x
        return colar

    def rodarEsquerda(self,colar):
        x = colar[0]
        for i in range(len(colar)-1):
            colar[i] = colar[i+1]
        colar[len(colar)-1] = x
        return colar

    def vetorCores(self):
        dic = {self.colar1[0]:1}
        for a in range(1, len(self.colar1)) :
                if self.colar1[a] not in dic :
                    dic.update({self.colar1[a]: 1})
                else :
                    dic[self.colar1[a]] = dic[self.colar1[a]] + 1
        for a in range(len(self.colar2)) :
            if (a != 0) & (a != 4) :
                if self.colar2[a] not in dic :
                    dic.update({self.colar2[a]: 1})
                else :
                    dic[self.colar2[a]] = dic[self.colar2[a]] + 1
        return dic 
     
class PuzzleColares(Problem):
    
    def __init__(self, initial=PuzzleCores()):
        
        a = initial.vetorCores()
        ehValido = False
        
        if (len(initial.colar1) == 20) & (len(initial.colar2) == 20) & (
                len(a) == 4) & (initial.colar1[0] == initial.colar2[0]) & (initial.colar1[4] == initial.colar2[4]) :
            for x in a :
                if (a.get(x) == 10) | (a.get(x) == 9) :
                    ehValido = True
                else :
                    ehValido = False
                    break
        if ehValido :
            self.initial = initial
        else :
            sys.exit("O estado inicial nao eh valido")
            
    def actions(self, state):
        return ["Rodar ColarEsquerda Esquerda","Rodar ColarEsquerda Direita","Rodar ColarDireita Esquerda","Rodar ColarDireita Direita"]

    def result(self, state, action):
        x = action.split()
        a = state.colar1.copy()
        b = state.colar2.copy()
        if x[1] == "ColarEsquerda":
            if x[2] == "Esquerda":
                a = state.rodarDireita(state.colar1.copy())
                b[0] = a[0]
                b[4] = a[4]
            else:
                a = state.rodarEsquerda(state.colar1.copy())
                b[0] = a[0]
                b[4] = a[4]
        elif x[1] == "ColarDireita":
            if x[2] == "Esquerda":
                b = state.rodarEsquerda(state.colar2.copy())
                a[0] = b[0]
                a[4] = b[4]
            else:
                b = state.rodarDireita(state.colar2.copy())
                a[0] = b[0]
                a[4] = b[4]
        return PuzzleCores(a, b)

    def goal_tester(self,colar):
        cores = [colar[0]]
        y = colar[0]
        aux = False
        for x in colar[1:]:
            if (cores[0] == x) & (y != x):
                aux = True
            if aux:
                if x != cores[0]:
                    return False
            if (x in cores) & (y != x) & (not aux):
                return False
            if not x in cores:
                cores.append(x)
                y = x
        return True

    def goal_test(self,state):
        return self.goal_tester(state.colar1) & self.goal_tester(state.colar2)
    
    def __eq__(self,estado):
        return (estado.initial.getColar1() == self.initial.getColar1()) & (
            estado.initial.getColar2() == self.initial.getColar2())
    
    def rotate(self,l,n):
        return l[n:] + l[:n]
    
    def display(self, state):
     
        x = self.rotate(state.colar1, 7)
        y = self.rotate(state.colar2, 7)
        
        aux1, aux3, aux4 = "", "", ""
        maxLen = max([len(a) for a in x])
        
        for i in range(len(x)):
            if (len(x[i]) < maxLen) :
                aux1 = " " * (maxLen - len(x[i]))
                
            if (i != 0) & (i != 10) :
                if (len(x[len(x)-i]) < maxLen) :
                    aux3 = " " * (maxLen - len(x[len(x)-i]))
                if (len(y[len(y)-i]) < maxLen) :
                    aux4 = " " * (maxLen - len(y[len(y)-i]))
                
            if (i == 0) | (i == 10):
                print (" "*20 + x[i] + aux1 + " "*25 + y[i])
            if (i == 1) | (i == 9):
                print (" "*16 + x[i] + aux1 + " "*5 + x[len(x)-i] + aux3 + " "*15 + 
                        y[len(y)-i] + aux4 + " "*5 + y[i])
            if (i == 2) | (i == 8):
                print (" "*12 + x[i] + aux1 + " "*15 + x[len(x)-i] + aux3 + " "*5 +
                        y[len(y)-i]+ aux4 + " "*15 + y[i])
            if (i == 3) | (i == 7):
                print (" "*8 + x[i] + aux1 + " "*25 + x[len(x)-i] + aux3 + " "*25 +
                       y[i])
            if (i == 4) | (i == 6):
                print (" "*4 + x[i] + aux1 + " "*25 + y[len(y)-i] + aux4 + " "*3 + 
                       x[len(x)-i] + aux3 + " "*25 + y[i])
            if i == 5:
                print (x[i] + aux1 + " "*25 + y[len(y)-i] + aux4 + " "*12 + 
                       x[len(x)-i] + aux3 + " "*25 + y[i])
        return ""
def exec(p,estado,accoes):
    """ Executa uma sequência de acções a partir do estado
        devolve um par (estado, custo) depois de imprimir
    """
    custo = 0
    for a in accoes:
        seg = p.result(estado,a)
        custo = p.path_cost(custo,estado,a,seg)
        estado = seg
    return (estado,custo)


x = PuzzleCores()
p = PuzzleColares(x)

print("Display do estado inicial: ")
p.display(p.initial)

print("\nVerifica se o estado inicial satisfaz a solucao do problema: ")
print(p.goal_test(p.initial), "\n")

print("Sao aplicadas diversas acoes a um estado: ")
acoes =  ["Rodar ColarEsquerda Esquerda","Rodar ColarEsquerda Esquerda",
          "Rodar ColarDireita Direita"]
a = exec(p, p.initial, acoes)
print(p.display(a[0]), "\nCusto de ter feito o que esta em acoes: ", a[1])

x1 = PuzzleCores()
p1 = PuzzleColares(x1)
print("\nVerifica que dois puzzles sao iguais: ", p.__eq__(p1))
acoes1 =  ["Rodar ColarDireita Direita"]
b = p1.result(p1.initial, acoes1[0])
print("\nVerifica se depois de rodar chegou a solucao: ", p1.goal_test(b))
print(p1.display(b))

acoes2 =  ["Rodar ColarDireita Esquerda"]
b1 = p1.result(b, acoes2[0])
print("\nVerifica se reverter as mudancas do anterior se volta" +
      "a satisfazer a solucao do problema:", p1.goal_test(b1))
print(p1.display(b1))

#print(p.goal_test(p.initial))
#p.display(p.initial)
#banana = p.result(p.initial, "Rodar ColarEsquerda Esquerda")
#print(banana)
#p.display(banana)
#print(p.initial)