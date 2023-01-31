import random as rd

class Graph:
    def __init__(self,**kargs): #each vertex is numbered 1 to N
        if len(kargs.keys()) != 0:
            if kargs["random"]:
                self.NDict = {}
                for i in range(1,kargs["N"]+1):
                    self.NDict[i] = []
                V = list(self.NDict.keys())
                edges = []
                while len(edges) < kargs["E"]:
                    pair = set(rd.sample(V,2))
                    if pair not in edges:
                        edges.append(pair)
                    
                for e in edges:
                    edge = list(e)
                    self.NDict[edge[0]].append(edge[1])
                    self.NDict[edge[1]].append(edge[0])
        else:     
            self.NDict = kargs["neibour_dict"]

    def get_neibours(self,i):
        return self.NDict[i]
    
    def get_vertices(self):
        return list(self.NDict.keys())
    
    def BFS(self,s):
        V = self.get_vertices()
        if s not in V:
            raise Exception
        layers = [[s]]
        discovered = [s]
        while True:
            layer = []
            for x in layers[-1]:
                neibours = self.get_neibours(x)
                for n in neibours:
                    if n not in discovered:
                        discovered.append(n)
                        layer.append(n)
            if len(layer) != 0:
                layers.append(layer)
            else:
                for i in range(len(layers)):
                    print("Layer",i,":",layers[i])
                return layers 




G = Graph(random = True, N = 6, E = 12)
print(G.NDict)
G.BFS(1)

    


