#
#
# SECCIONES DEL PROGRAMA
# ----------------------
# 1)Imports
# 2)Funcions
# 3)Variables globals
# 4)Inicio programa
#

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
    for ladrillo in muros:
        l[ladrillo[0]][ladrillo[1]] = "X"

def mostrar_laberinto(titulo, laberinto):
    print(colorama.Fore.YELLOW + "*** " + titulo + " ***")
    for fila in laberinto:
        for celda in fila:
            if (celda == " "):
                print(colorama.Back.WHITE + "  ",end="")
            elif(celda== "E"):
                print(colorama.Back.GREEN +"E ",end="")
            elif(celda== "S"):
                print(colorama.Back.GREEN + "S ", end="")
            elif(celda=="X"):
                print(colorama.Back.RED + " X", end="")
            elif(celda=="·"):
                print(colorama.Back.YELLOW + " ··", end="")
            else:
                print("Error en el laberinto --> Símbolo inesperado!")
        print(colorama.Back.BLACK + colorama.Fore.WHITE)

    print(colorama.Back.BLACK + colorama.Fore.WHITE)

def poner_casilla_entrada(lab,entrada):
    lab[entrada[0]][entrada[1]]="E"
    

def poner_casilla_salida(lab,salida):
    lab[salida[0]][salida[1]]="S"
    

# Por cada paso que no sea la entrada/salida pondremos "·"
def ajustar_camino_sobre_laberinto(laberinto, entrada, salida, camino_salida):
    for paso in camino_salida:
        if(paso != entrada) and (paso != salida):
            laberinto[paso[0]][paso[1]] = "·"


# Creacion del diccionario para guardar todas las casillas usadas
# y para no volverlas a visitar
def crear_diccionario_casillas(dim):
    # Creamos un diccionario con todas las casillas del 
    # laberinto y un indicador booleano (False) de q no se ha usado
    
    casillas= {}

    for num_fila in range(0,dim):
        for num_columna in range(0,dim):
            #Añadir una nueva casilla al diccionario
            casillas[str(num_fila)+ "-" + str(num_columna)]=False
    
    return casillas



# En principio para cada casilla son posibles cuatro pasos, 
# (arriba,abajo,derecha,izquierda),
# pero hay que descartar los siguientes casos:
# - Que la casilla esté fuera del laberinto
# - Que en la casilla haya un muro ("X")
# - Que sea la casilla de entrada al laberintoo ("E")
# - Que la casilla haya  sido visitada previamente. Para esto
# usaremos el diccionario casillas_usadas
#False --> opcion no valida
# True --> es el paso posible 
def paso_posible(laberinto, casillas_usadas, dim, num_fila, num_columna):
    # Comprobar si fila fuera de rango
    if (num_fila<0) or (num_columna>=dim):
      return False

    # Comprobar si columna fuera de rango
    if(num_columna<0) or (num_columna>=dim):
        return False

    # Comprobar si hay un ladrillo
    if (laberinto[num_fila][num_columna] == "X"):
        return False

    # Comprobar si es la casilla de entrada
    if (laberinto[num_fila][num_columna] == "E"):
        return False

    # Comprobar si esta casilla ya se descarto
    if (casillas_usadas[str(num_fila)+"-"+str(num_columna)]):
        return False

    return True

#  Hay  4 posibles pasos, pero hay bastantes casos en los
# que  no tenemos cuatro opciones ya que estan fuera de la pantalla
def dar_un_paso(laberinto,casillas_usadas,dim,pos_actual):
    num_fila= pos_actual[0]
    num_columna= pos_actual[1]
    #  Explorar ABAJO
    if paso_posible(laberinto, casillas_usadas, dim, num_fila+1, num_columna):
        return(num_fila+1,num_columna)

    # Explorar DERECHA
    if paso_posible(laberinto, casillas_usadas, dim, num_fila, num_columna+1):
        return (num_fila, num_columna+1)

    # Explorar IZQUIERDA
    if paso_posible(laberinto, casillas_usadas, dim, num_fila, num_columna-1):
        return (num_fila, num_columna-1)

    # Explorar ARRIBA
    if paso_posible(laberinto, casillas_usadas, dim, num_fila-1, num_columna):
        return (num_fila-1, num_columna)

    return ()

# Hay que marcar cada casilla estará marcada como usada después de dar un paso
def marcar_casilla_como_usada(casillas_usadas,casilla):
    num_fila=casilla[0]
    num_columna=casilla[1]
    casillas_usadas[str(num_fila)+ "-" + str(num_columna)]= True


def buscar_camino_salida(laberinto,casillas_usadas,dim):
    # Damos por hecho que la entrada siempre está  en sus coordenadas 0,0.
    pos_actual = (0,0)
    camino= [(0,0)]
    casillas_usadas["0-0"] = True

    salida = False
    while (not salida) and  (len(camino)>0):
        nuevo_paso = dar_un_paso(laberinto, casillas_usadas, dim, pos_actual)
        if (len(nuevo_paso) == 0):
            # Eliminar la ultima posicion del camino porque sabemos  que no 
            # conduce a la salida
            camino.pop()

            # Convertir el ultimo paso del camino en posicion actual
            # Al ultimo elemento de una  lista se accede con el indice -1
            pos_actual = camino[-1]
        else:
            camino.append(nuevo_paso)
            marcar_casilla_como_usada(casillas_usadas, nuevo_paso)
            pos_actual=nuevo_paso

        # Marcar casilla como usada en el diccionario
        salida= laberinto[pos_actual[0]][pos_actual[1]] == "S" 

    return camino





#### V A R I A B L E S   G L O B A L E S ####

# Creacion tupla con las posiciones del muro
muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1),
        (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Ancho y alto del laberinto ya que se supone cuadrado
dimension= 6

# Posicion de entrada y salida del laberinto
entrada=(0,0)
salida=(5,5)


####  I N I C I O    P R O G R A M A  ####
clear()

laberinto= crear_laberinto_vacio(dimension)
# mostrar_laberinto("Laberinto vacio", laberinto)

ajustar_muros_laberinto(laberinto,muros)
# mostrar_laberinto("Laberinto con muros", laberinto)

mostrar_laberinto("Laberinto completo", laberinto)
poner_casilla_entrada(laberinto,entrada)
poner_casilla_salida(laberinto,salida)

casillas_usadas = crear_diccionario_casillas(dimension)

camino_salida = buscar_camino_salida(laberinto, casillas_usadas, dimension)

ajustar_camino_sobre_laberinto(laberinto,entrada,salida,camino_salida)
mostrar_laberinto("Camino de salida",laberinto)

print(camino_salida)