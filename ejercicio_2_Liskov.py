class Figura: # Clase maestra
    # Funcion para que cada figura "hija" pueda obtener su area
    def obtener_area(self):
        pass

class Rectangulo(Figura): # Clase hija
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # Llamamos a la funcion de la clase maestra
    def obtener_area(self):
        return self.ancho * self.alto
    
    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto

class Cuadrado(Figura): # Clase hija
    def __init__(self, lado):
        self.lado = lado

    def set_lado(self, lado):
        self.lado = lado

    # Llamamos a la funcion de la clase maestra
    def obtener_area(self):
        return self.lado * self.lado
    
def imprimir_area(figura : Figura):
    print(f"El area es: {figura.obtener_area()}")

cuadrado = Cuadrado(4)
rectangulo = Rectangulo(4, 5)

area_cuadrado = imprimir_area(cuadrado)
area_rectangulo = imprimir_area(rectangulo)