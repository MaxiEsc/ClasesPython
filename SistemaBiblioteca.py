

from Biblioteca import Biblioteca
from Libro import (Libro)

bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {bibliotecaNacional.nombre} ***')

# Definicion de libros
libro1 = Libro('Cien años', 'Anonimo', 'Comedia')
libro2 = Libro('Don Quijote', 'Anonimo', 'Comedia')
libro3 = Libro('El amor en los tiempos de guerra', 'Anonimo', 'Comedia')
libro4 = Libro('Pedro Páramo', 'Anonimo', 'Ficción')
libro5 = Libro('Pantaleón', 'Anonimo', 'Comedia')

# Agregas los libros a la biblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

# Buscar libros por autor
autor = 'Anonimo'
print(f'\nLibros de {autor}')
bibliotecaNacional.buscar_libros_por_autor(autor)

# Buscar libros por género
genero = 'Ficción'
print(f'\nLibros de {genero}')
bibliotecaNacional.buscar_libros_por_genero(genero)

# Mostrar todos los libros de la biblioteca
bibliotecaNacional.mostrar_todos_los_libros()