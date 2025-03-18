'''
A diferencia de otros lenguajes de programacion orientados a objetos, Python permite ciertas anotaciones que
le permiten un poco mas de maniobrabilidad para el mismo en cuestion... Por asi decirlo...
Son simples anotaciones que vuelven mas legibles el acceso a los atributos dentro del main
es como si simplemente fueran publicos.
'''


# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._color = color  # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    @property  # Definir el metodo get de manera mas pythonica Interesante anotaciones
    def marca(self):
        return self._marca

    # Anotaciones para la ejecucion correcta segun python enbase a setters
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Definir el metodo get de manera mas pythonica Interesante anotaciones
    @property
    def modelo(self):
        return self._modelo

    # Anotaciones para la ejecucion correcta segun python enbase a setters
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    # Definir el metodo get de manera mas pythonica Interesante anotaciones
    @property
    def color(self):
        return self._color

    # Anotaciones para la ejecucion correcta segun python enbase a setters
    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos, aunque con la anotacion es como si se puedieran acceder a los mismos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Azul 2'
    coche1.conducir()
    # Atributo de marca del coche 1
    coche1.marca = 'Toyota 3'
    print(f'Atributo marca coche1: {coche1.marca}')
