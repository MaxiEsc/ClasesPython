'''
En este caso Vemos que Python a diferencia de Java, Python no posee SObrecarga de constructores por lo que
Lamentablemente no es una idea por lo que Python solamente toma el ultimo constructor escrito el resto es ignorado

Pero aun se puede llevar los famosos valores por default como el tema de las funciones. Pero ojo es no implica que los
objetos puedan estar vacios. por lo que no puedes sumar un 7 mas la nada. Eso explota.
Por lo que si se crea un objeto sin siquiera los parametros por default entonces al menos cargar las variables en memoria
para que el tipo de dato pueda trabajar
'''

class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segundo objeto
    print('Segundo objeto')
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer objeto
    print('Tercer objeto')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()
    # Cuarto objeto
    print('Cuarto objeto')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    # Quinto objeto
    print('Quinto objeto')
    #Interesante dato que python puede asignar el valor de los operando indistinto al orden gracias a la declaracion del constructor
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()
