#
#
# SECCIONES DEL PROGRAMA
# ----------------------
# 1)Imports
# 2)Funciones
# 3)Variables globales
# 4)Inicio programa
#

#1) I M P O R T S 
import os
import colorama

####
#2) F U N C I O N E S 
####



def clear():
    # Limpiar la terminal
    # No funciona al ejecutar en ventana interactiva 
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

def ajustar_muros_laberinto(laberinto, muros):
    # Pone una  "X" en las casilla donde esta especificado
    # que debe haber un muro --> Casillas "NO transitables"
    for ladrillo in muros:
        laberinto[ladrillo[0]][ladrillo[1]] = "X"

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
                print(colorama.Back.RED + "X ", end="")
            elif(celda=="·"):
                print(colorama.Back.YELLOW + "··", end="")
            else:
                print("Error en el laberinto --> Símbolo inesperado!")

        print(colorama.Back.BLACK + colorama.Fore.WHITE)

    print(colorama.Back.BLACK + colorama.Fore.WHITE)

def poner_casilla_entrada(lab,entrada):
    # Pone una  "E" en la casilla de entrada al laberinto
    lab[entrada[0]][entrada[1]]="E"
    
def poner_casilla_salida(lab,salida):
    # Pone una "S" en la casilla de salida del laberinto
    lab[salida[0]][salida[1]]="S"
    


def ajustar_camino_sobre_laberinto(laberinto,entrada,salida,camino_salida):
    # Por cada paso que no sea la entrada/salida pondremos "·" para 
    # visualizarlo de una forma mas grafica.
    # Para ello usamos la lista de "camino_salida" que contiene las 
    # coordenadas de todas las celdas q forman partte del camino de salida.
    # A cada celda que forma parte del camino de salida la he denominado "paso"
    for paso in camino_salida:
        if(paso != entrada) and (paso != salida):
            laberinto[paso[0]][paso[1]] = "·"



def crear_diccionario_casillas(dim):
    # Creacion del diccionario para guardar todas las casillas usadas
    # y para no volverlas a visitar
    # Creamos un diccionario con todas las casillas del 
    # laberinto y un indicador booleano (False) de q no se ha usado
    
    casillas= {}

    for num_fila in range(0,dim):
        for num_columna in range(0,dim):
            #Añadir una nueva casilla al diccionario
            casillas[str(num_fila)+"-"+str(num_columna)] = False
    
    return casillas

def paso_posible(laberinto, casillas_usadas, dim, num_fila, num_columna): 
    # El objetivo de esta funcion es validar si una casilla
    # puede formar parte del camino de salida.
    # En principio para cada casilla son posibles cuatro pasos, 
    # (arriba,abajo,derecha,izquierda),
    # pero, para que la casilla forme parte hay que descartar los siguientes casos:
    # - Que la casilla esté fuera del laberinto
    # - Que en la casilla haya un muro ("X")
    # - Que sea la casilla de entrada al laberintoo ("E")
    # - Que la casilla haya  sido visitada previamente. Para esto
    # usaremos el diccionario casillas_usadas
    #False --> opcion no valida
    # True --> es el paso posible 
   
    # Comprobar si fila fuera de rango
    if (num_fila < 0) or (num_fila >= dim):
        return False

    # Comprobar si columna fuera de rango
    if (num_columna < 0) or (num_columna >= dim):
        return False

    # Comprobar si hay un ladrillo
    if (laberinto[num_fila][num_columna] == "X"):
        return False

    # Comprobar si es la casilla de entrada
    if (laberinto[num_fila][num_columna] == "E"):
        return False

    # Comprobar si esta casilla ya se exploró
    if (casillas_usadas[str(num_fila)+"-"+str(num_columna)]):
        return False

    # Como no se dan las condiciones anteriores significa que la 
    # casilla es candidata a ser parte del camino de salida y por 
    # ello devolveremos True.
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
    # Funcion principal del programa y su objetivo es
    # calcular un camino de salida entre los que pueda haber.
    #Empezamos directamente en la casilla de entrada
    # Damos por hecho que la entrada siempre está en la esquina superior izquierda --> coordenadas 0,0.
    pos_actual = (0,0)
    camino= [(0, 0)]
    nueva_direccion= ""
    direccion_salida= ["ENTRADA"]
    casillas_usadas["0-0"] = True

    # Indicamos que todavia no hemos encontrado el camino de salida
    # El bucle while iterará mientras no se haya encontrado la salida y mientras existan
    # celdas que explorar si conducen a una salida.
    salida = False
    while (not salida) and (len(camino)>0):
        #Damos un paso en busca de la salida
        nuevo_paso = dar_un_paso(laberinto, casillas_usadas, dim, pos_actual)
        if (len(nuevo_paso) == 0):
            # No hemos podido desde la celda actual -> len(nuevo_paso) == 0

            # Eliminar la ultima posicion del camino porque sabemos  que no 
            # conduce a la salida
            camino.pop()
            direccion_salida.pop()

            # Retrocedemos un paso en el camino: Convertir el ultimo paso del camino en posicion actual
            # Al ultimo elemento de una lista se accede con el indice -1
            pos_actual = camino[-1]
        else:
            # Hemos encontrado una celda para explorar si nos lleva a la salida
            
            # Añadimos la nueva celda al camino de salida
            camino.append(nuevo_paso)
            direccion_salida.append(nueva_direccion)

            # Marcamos la casilla como usada para no volverla a explorar
            marcar_casilla_como_usada(casillas_usadas, nuevo_paso)
            pos_actual=nuevo_paso

        # Marcar casilla como usada en el diccionario
        salida= laberinto[pos_actual[0]][pos_actual[1]] == "S" 

    return camino, direccion_salida




####
#3) V A R I A B L E S   G L O B A L E S
####

# Creacion tupla con las posiciones del muro
muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1),
        (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Ancho y alto del laberinto ya que se supone cuadrado
dimension= 5

# Posicion de entrada y salida del laberinto
entrada=(0,0)
salida=(4,4)

# Camino de slida --> Lista de coordenads de casillas que conducen a la salida
caminoo_salida= []

# Direccion de salida --> Instrucciones para ir hasta la salida en forma de direccion
direccion_salida= []

####
#4) I N I C I O    P R O G R A M A
####

clear()

# Crear el laberinto con muros, entrada y salida
laberinto= crear_laberinto_vacio(dimension)
ajustar_muros_laberinto(laberinto,muros)
poner_casilla_entrada(laberinto,entrada)
poner_casilla_salida(laberinto,salida)
mostrar_laberinto("Laberinto", laberinto)

#Crear un diccionario que se usara para saber las casillas que ya se han explorado
# con la finalidad de evitar ciclos en lo que se vuelva a explorar una casilla
# una y otra vez ...
casillas_usadas = crear_diccionario_casillas(dimension)

# mostrar_laberinto("Laberinto vacio", laberinto)
# mostrar_laberinto("Laberinto con muros", laberinto)


# Funcion principal
camino_salida, direccion_salida = buscar_camino_salida(laberinto, casillas_usadas, dimension)

# Marca el camino de salida  sobre el laberinto
ajustar_camino_sobre_laberinto(laberinto,entrada,salida,camino_salida)
mostrar_laberinto("Camino de salida",laberinto)

# Mostrar las listas con información del camino de salida
print(colorama.Fore.YELLOW +
      "*** Dirección de salida: Dirección ha seguir para salir ***" + colorama.Fore.WHITE)
print(direccion_salida)
print()
print(colorama.Fore.YELLOW +
      "*** Camino de salida: celdas que forman parte del camino de salida ***" + colorama.Fore.WHITE)
print(camino_salida)