import os
import colorama

#### F U N C I O N E S ####
# Limpiar la terminal
# No funciona al ejecutar en ventana interactiva 
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# El tablero es una lista de listas
# !!!!!!RECORDATORIO¡¡¡¡¡
# -------------------------
# Cada variable de la funcion se llama variable local, las
# variables globales no tienen nada que ver con las locales.
# Las variables locales de una funcion no tienen nada que ver con
# las variables locales de otra funcion.

def crear_laberinto_vacio(dim):
    # Creamos el laberinto como una lista vacia por ahora
    l= []

    for num_fila in range(0, dim):
        # Creamos una fila como una lista vacia por ahora
        fila=[]

        #Rellenamos la fila
        for num_columna in range(0, dim):
            #Añadir elementos a la nueva fila
            fila.append(" ")

        # Añadir nueva fila al tablero
        l.append(fila)
    
    return l

# Pone las "X" en el laberinto donde esta especificado que debe haber un muro
def ajustar_muros_laberinto(l, muros):
    for m in muros:
        l[m[0]] [m[1]] = "X"

def mostrar_laberinto(titulo, laberinto):
    print("*** " + titulo + " ***")
    for fila in laberinto:
        for casilla in fila:
            if (casilla == " "):
                print(colorama.Back.WHITE + " ",end=" ")
            else:
                print(colorama.Back.RED + " ", end=" ")
        print(colorama.Back.BLACK)

    print(colorama.Back.BLACK)


#### V A R I A B L E S   G L O B A L E S ####
muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1),
        (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Ancho y alto del laberinto ya que se supone cuadrado
dimension= 5

clear()


####  I N I C I O    P R O G R A M A  ####
# Creacion del laberinto sin muros
laberinto= crear_laberinto_vacio(dimension)
mostrar_laberinto("Laberinto vacio", laberinto)

# Creacion del laberinto con muros
ajustar_muros_laberinto(laberinto,muros)
mostrar_laberinto("Laberinto con muros", laberinto)