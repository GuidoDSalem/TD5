class Nodo:
    def __init__(self,nombre:str,valor) -> None:
        self.nombre:str = nombre
        self.valor = valor
        self.vecinos = {}

    def agregarVecino(self,nodo,valor=1):
        if self.esVecino(nodo):
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
        + "\n\tVALOR: " + str(self.valor) \
        + "\n\t\tVECINOS: "
        for nodo in self.vecinos:
            value += str(nodo)

        return value

