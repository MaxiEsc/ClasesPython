'''
En este ejercicio se pondra en practicas dos ideas conceptuales
los atributos de clase y los atributos de instancia:
Los atributos de instancia son aquellos atributos que se realacionan con la creacion de los objetos en cuestion.
osea los objetos que hemos trabajado desde siempre, donde las modificaciones de los atributos que representadas
en el mismo objeto por ejemplo auto1 de la clase auta puede tener un atributo de color y este sea amarillo
en ese caso estamos trabajando con atributos de instacia
la idea de "El atributo de clase" es la simplemente la modificaciones de los atributos de una clase en cuestion

'''

class Persona:
    #En este caso seria un atributo de clase podriamos tomarlo como un ID de clase
    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa principal
if __name__ == '__main__':
    print(f'*** Atributos de Clase ***')
    print(f'Atributo de Clase: {Persona.atributo_clase}')
    # Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de Clase: {Persona.atributo_clase}')

    # Creamos un objeto persona1
    persona1 = Persona(15)
    print(f'Atributo de Clase desde persona1: {persona1.atributo_clase}')
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')

    # Creamos un objeto persona2
    persona2 = Persona(30)
    print(f'Atributo de Clase desde persona2: {persona2.atributo_clase}')
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')
