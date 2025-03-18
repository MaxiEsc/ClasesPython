'''
Como vemos Python tambien es un lenguaje orientado a objetos como JAVA, solo que es menos restrictivo.
'''

# Definicion de una clase
class Persona:


    #Self Se utiliza como el this. en java
    #Setters
    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    #Getters
    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

# Creacion de objetos mas su determinado Main
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona()  # Crea un objeto vacio en memoria, se realiza de la misma forma de declaracion que Java
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona() # Crea un objeto vacio en memoria
    persona2.inicializar_persona('Ian', 'Sánchez')
    persona2.mostrar_persona()

    