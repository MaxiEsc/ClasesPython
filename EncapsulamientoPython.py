'''
El tema de encapsulamiento, Python al ser un lenguaje orientado a objeto permite la seguridad de acuerdo a la nomina
de los legunajes orientados a objetos.
En este caso para proteger atributos no se usan las respectivas palabras como en c++ o en java

self._algo #Atributo protegido
self.__algo # atributo privado.

Con esto ya podemos crear los famosos getters and setters

'''

# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca # Publico
        self._modelo = modelo # Protegido
        self.__color = color # Privado

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2'  # Se puede y esta feo el acceder asi al atributo protegido... Esto no es una buena practica
    coche1.__color = 'Azul 2'  # igoro la modificacion Gracias al ser un atributo privado
    coche1._Coche__color = 'Azul 3'  #... Porque python permite esto?? Rompe la idea del encapsulamiento... Es una mala practica
    coche1.conducir()