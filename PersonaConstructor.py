'''
El constructor un metodo de gran importancia como en los demas funciones de los leguajes orientados a objetos
con el constructos este no se necesitara un metodo dedicado a la inicializacion de objetos y se evitaran errores
innecesarios

Este se declara de la siguiente manera

class algo:
    def __init__(self, par1, par2,...,parX)
    self.par1 = par1
    self.par2 = par2
'''


# Definicion de una clase
class Persona:

    #  Constructor
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')


# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta')  # Crea un objeto vacio en memoria
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sánchez')  # Crea un objeto vacio en memoria
    persona2.mostrar_persona()
