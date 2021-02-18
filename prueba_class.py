class persona():
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura

    def presentacion(self):
        print("su nombre es: ", self.nombre)




pepe = persona("juan", 14, 15)

pepe.presentacion()