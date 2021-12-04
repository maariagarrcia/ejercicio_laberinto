import os

#### F U N C I O N E S ####
# Limpiar la terminal
# No funciona al ejecutar en ventana interactiva :(
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# El tablero es una lista de de listas
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



def ajustar_muros_laberinto(l,muros):

def mostrar_laberinto(titulo,laberinto):






#### V A R I A B L E S   G L O B A L E S ####

muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1),
        (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Ancho y alto del laberinto ya que se supone cuadrado
dimension= 5

clear()


#### I N I C I O    P R O G R A M A  ####
# Creacion del laberinto sin muros
laberinto= crear_laberinto_vacio(dimension)
mostrar_laberinto("Laberinto vacio", laberinto)

# Creacion del laberinto con muros
ajustar_muros_laberinto(laberinto,muros)
mostrar_laberinto("Laberinto con muros", laberinto)
