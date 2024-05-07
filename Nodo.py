class Nodo:
    def __init__(self,nombre:str,valor) -> None:
        self.nombre:str = nombre
        self.valor = valor
        self.vecinos = {}

    def agregarVecino(self,nodo,valor=1):
        if self.esVecino(nodo):
            # Ya es vecino, no hacer nada
            return
        else:
            self.vecinos[nodo.nombre] = valor

    def eliminarVecino(self,nodo_):
        for nodo in self.vecinos:
            if nodo == nodo_.nombre:
                self.vecinos.pop(nodo)
            i += 1

    def setValue(self,newValue):
        self.nombre = newValue
    
    def esVecino(self,nombre) -> bool:
        return nombre in self.vecinos
            

    def __str__(self):
        value = "NOMBRE: " + str(self.nombre) \
        + "\nVALOR: " + str(self.valor) \
        + "\nVECINOS: \n"
        for vecino,peso in self.vecinos.items():
            value += str(vecino)+ ": " + str(peso) + "\n"

        return value

