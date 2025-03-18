'''
Las direcciones de memoria aqui mismo tenemos un ejercicio haciendo enfasis de la direcciones de memoria por lo que podemos apreciar
la idea de la los cambios de la memoria. Pero podemos asociar la idea de Punteros de c++ en donde la idea de la memoria es interesante.
por lo que es interesante que el lenguaje python asigna los objetos creados en el lugar de memoria ram que tenga disponible.
En otras palabras nada de creaciones de variables temporales como lo manejan las funciones el self maneja el objeto directo de la memoria
sin excepcion por lo que es interesante esto no hubo ningun acercamiento a punteros como lo fue pero es la misma idea.
Puesto que en c++ se maneja la idea de que cada vez que un funcion es creada este si lleva una variable esta lleva una copia de la misma
pero no la misma. Por lo que es interesante que el self permite directamente pasar la referencia.
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
        print(f'Dir. mem self: {id(self)}')
        print(f'Dir. mem hex self: {hex(id(self))}')


# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta')  # Crea un objeto vacio en memoria
    persona1.mostrar_persona()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem hex persona1: {hex(id(persona1))}')

    # Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sánchez') # Crea un objeto vacio en memoria
    #persona2.inicializar_persona('Ian', 'Sánchez')
    persona2.mostrar_persona()
    print(f'Dir. mem persona2: {id(persona2)}')
    print(f'Dir. mem hex persona2: {hex(id(persona2))}')
