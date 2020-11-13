class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Forma:
    def __init__(self, color, x, y, nombre):
        self.color = color
        self.centro = Punto(x,y)
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre, self.color, self.centro.x, self.centro.y)

    def getColor(self):
        return self.color

    def cambiaColor(self,color):
        self.color = color

    def mover(self,newX,newY):
        self.centro = Punto(newX,newY)


class Rectangulo(Forma):
    def __init__(self,color, x, y, ladoMenor,ladoMayor):
        Forma.__init__(self,color, x, y, "Rectangulo")

        self.ladoMenor = ladoMenor
        self.ladoMayor = ladoMayor

    def imprimir(self):
        Forma.imprimir(self)
        print("Lado Menor: ",self.ladoMenor," Lado Mayor:",self.ladoMayor)

    def getArea(self):
        print(self.ladoMenor*self.ladoMayor)

    def getPerimetro(self):
        print(self.ladoMenor*2 + self.ladoMayor*2)

    def escalar(self,escala):
        self.ladoMenor = self.ladoMenor * escala
        self.ladoMayor = self.ladoMayor * escala


class Elipse(Forma):
    def __init__(self,color, x, y,radioMayor,radioMenor):
        Forma.__init__(self, color, x, y, "Elipse")
        self.radioMenor = radioMenor
        self.radioMayor = radioMayor

    def imprimir(self):
        Forma.imprimir(self)
        print("Radio menor: ", self.radioMenor, " Radio Mayor: ",self.radioMayor)


class Cuadrado(Rectangulo):
    def __init__(self,color, x, y, lado):
        Rectangulo.__init__(self,color, x, y, lado, lado)
        self.nombre = "Cuadrado"

    def imprimir(self):
        Forma.imprimir(self)
        print("Lado: ", self.lado)

class Circulo(Elipse):
    def __init__(self,color, x, y, radio):
        Elipse.__init__(self,color, x, y,radio, radio)
        self.nombre = "Circulo"

    def imprimir(self):
        Forma.imprimir(self)
        print("Radio: ", self.radioMenor)

circ = Circulo("Blanco",5,5,10)
cuad = Cuadrado("Negro",20,20,3)

lista = [circ, cuad]

posCont = 0
for i in lista:
    i.color = "Verde"
    i.centro = Punto(posCont*2,posCont*2)
    posCont+1

