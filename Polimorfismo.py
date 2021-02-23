
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    #def avanza(self):
        #print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza() #aca aggararia el avanza de persona, eliminando los # de ciclista usaria el avanza de ciclista


if __name__ == '__main__':
    main()
