#### I N I C I O    P R O G R A M A  ####
# Creacion del laberinto sin muros
laberinto= crear_laberinto_vacio(dimension)
mostrar_laberinto("Laberinto vacio", laberinto)

# Creacion del laberinto con muros
ajustar_muros_laberinto(laberinto,muros)
mostrar_laberinto("Laberinto con muros", laberinto)
