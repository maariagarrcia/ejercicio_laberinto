import os

#### F U N C I O N E S ####
# Limpiar la terminal
# No funciona al ejecutar en ventana interactiva :(
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def crear_laberintoo_vacio(dim):

def ajustar_muros_laberinto(l,muros):

def mostrar_laberinto(titulo,laberinto):











#### I N I C I O    P R O G R A M A  ####
# Creacion del laberinto sin muros
laberinto= crear_laberinto_vacio(dimension)
mostrar_laberinto("Laberinto vacio", laberinto)

# Creacion del laberinto con muros
ajustar_muros_laberinto(laberinto,muros)
mostrar_laberinto("Laberinto con muros", laberinto)
