'''
Introduccion con los metodos de clase

Estos metodos se asocian solo con la clase a si misma y no con los obejtos en cuestion
Por lo que antes los metodos de instancia se realacionan con self. que son los parametros que uno deja en evidencia
la realzacion de metodos con instancia...
Pero ahora veamos la idea de los metodos de clase.

Entonces resumiendo siempre que estamos trabajando en el contexto de la clase hace referencia al contexto estatico
Lo interesante es que los objetos dentro del contexto dinamico si pueden acceder este tipo de anotaciones estaticas de la clase
pero no viceversa... igual tiene sentido la creacion de objeto ya la hace dinamica por lo que por sentido comun es imposible
accerder a un contexto que aun no se ha creado...
'''

class Persona:
    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod #En este codigo solicitamos el contador de personas como metodo de clase.
    def get_contador_personas_estatico():
        print('Método estático')
        return Persona.contador_personas

    @classmethod #Interesante forma de hacerlo mediante anotaciones de lenguaje de python
    def get_contador_personas_clase(cls): #Sin preguntarno nos asigna ese argumento 'cls' haciendo referencia a incluso mas metodos de clase con lo que ya estamos trabajando
        print('Método de clase')
        return cls.contador_personas


if __name__ == '__main__':
    print('----> Ejemplo Contador de Objetos de tipo Persona <----')
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    # Segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona (persona1): {persona1.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}') #Todo lo estatico es relacionado con la clase en esta seccion
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')