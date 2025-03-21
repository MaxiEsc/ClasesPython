'''
Interesante caracteristica. Esta fucionalidad permite agregar un atributo a un objeto ya creado a la clase de manera temporal
lo que permite el acceso un monton de posibilidades en cuestion.
osea con esta caracteristica es posible dar atriburos unicos a objetos que sean unicos durante el momento de ejecucion.
'''

# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Azul 2'

    # Intentar agregar un nuevo atributo solo funciona en el objeto coche1 con setattr
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo')
    coche1.nuevo_atributo2 = 'Valor nuevo atributo 2'
    print(f'Atributos del coche1: {coche1.__dict__}') #Gracias a esta line le podemos preguntar a python los atributos del objeto en cuestion
    coche1.conducir()
    print(coche1.nuevo_atributo)
    print(f'Nuevo atributo coche1 {coche1.nuevo_atributo2}')
    # Segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Blanco')
    coche2.conducir()
    print(f'Atributos del coche2: {coche2.__dict__}')
    #print(f'Nuevo atributo coche2 {coche2.nuevo_atributo}')
    #print(f'Nuevo atributo coche2 {coche2.nuevo_atributo2}')

