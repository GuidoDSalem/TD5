import Nodo
import numpy as np
from collections import deque


class Grafo:
    def __init__(self,nodos:list,enlaces:list):
        self.nodos = {}
        if nodos:
            self.fillNodos(nodos)
        self.generarEnlaces(enlaces)
    

    def fillNodos(self,nodos):
        for nodo in nodos:
            self.nodos[nodo.nombre] = nodo

    def belongs(self,nodo):
        return nodo in self.nodos

    def generarEnlaces(self, enlaces:dict):
        for (nodoA,nodoB),value in enlaces.items():
            self.nodos[nodoA.nombre].agregarVecino(self.nodos[nodoB.nombre],value)

    def agregarNodo(self,nodo:Nodo):
        self.nodos[nodo.nombre] = nodo
    
    def getNodo(self,nombre:str):
        return self.nodos[nombre]


    def agregarEnlace(self,nombreA:str,nombreB:str):
        nodoA:Nodo = self.getNodo(nombreA)
        nodoB:Nodo = self.getNodo(nombreB)
        nodoA.agregarVecino(nodoB)

    def eliminarNodo(self,nodo:Nodo):
        self.nodos.popitem(nodo.nombre)

    def eliminarEnlace(self,nombreA,nombreB):
        i = 0
        nodoA = self.getNodo(nombreA)
        for nodo in nodoA.vecinos:
            if(nodo.nombre == nombreB):
                nodoA.vecinos.remove(i)
            i += 1
    
    def BFS(self,nombreInicio):
        NO_DESCUBIERTO = 0
        DESCUBIERTO = 1
        PROCESADO = 2

        nodo = None
        if self.belongs(nombreInicio):
            nodo = self.nodos[nombreInicio]
        else:
            raise ValueError("No existe un nodo con ese Nombre")

        estadoNodos = {}
        for nodoName in self.nodos:
            estadoNodos[nodoName] = NO_DESCUBIERTO # False === "No descubierto"
        pendientes = deque()
        pendientes.append(nodo)

        while(len(pendientes) > 0):
            actualNode:Nodo = pendientes.popleft()
            for vecino in actualNode.vecinos.keys():
                if estadoNodos[vecino] == NO_DESCUBIERTO:
                    estadoNodos[vecino] = DESCUBIERTO
                    pendientes.append(self.nodos[vecino])
            estadoNodos[actualNode.nombre] = PROCESADO
            print(actualNode.nombre)
        print(estadoNodos)
    
    def DFS(self,nombreInicial):
        NO_DESCUBIERTO = 0
        DESCUBIERTO = 1
        PROCESADO = 2
        if nombreInicial in self.nodos:
            nodoActual = self.nodos[nombreInicial]
        else:
            raise ValueError(f"El Nodo {nombreInicial} no pertenece al Grafo")
        
        estados = {nodoName:NO_DESCUBIERTO for nodoName in self.nodos}
        pendientes = [] # STACK - PILA
        pendientes.append(nodoActual)
        estados[nodoActual.nombre] = DESCUBIERTO
        
        while len(pendientes) > 0:
            nodoActual = pendientes.pop()
            for vecino in nodoActual.vecinos.keys():
                if estados[vecino] == NO_DESCUBIERTO:
                    estados[vecino] = DESCUBIERTO
                    pendientes.append(self.nodos[vecino])
            estados[nodoActual.nombre] = PROCESADO
            print(nodoActual.nombre)
        
        print(estados)

    def Prim():


        return# Nodos, enlaces