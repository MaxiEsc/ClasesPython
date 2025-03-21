'''
la idea de "El atributo de clase" es la simplemente la modificaciones de los atributos de una clase en cuestion
Como mencionabamos anteriormente podemos entender en cuestion, en este caso utilizamos el constructor para modificar
el contador de clase de personas... Cabe recordar que informacion queda solo en memoria.

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

if __name__ == '__main__':
    print('---> Ejemplo Contador de Objetos de tipo Persona <---')
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    # Segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_personas}')