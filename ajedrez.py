
# Integrantes:
# - Vicente René Cartes Cortés
# - Alexis Andrés Sotomayor Saldivia
# - Cristofer Luis Mamani Marino
# - Guido Esteban Aravena Retamal


def esPosicionValida(x, y, tablero):
    if x > tablero or x < 1 or y > tablero or y < 1:
        return False
    return True


def posiblesMovimientos(puntosPartida, tablero):

    # Funcion que toma una lista de puntos de partida y entrega una lista
    # de todos los puntos a los cuales se puede llegar con un movimiento desde
    # cada uno de los puntos de partida

    movimientos = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    puntosLlegada = list()

    for punto in puntosPartida:
        for mov in movimientos:
            nuevaX = punto[0] + mov[0]
            nuevaY = punto[1] + mov[1]

            if esPosicionValida(nuevaX, nuevaY, tablero):
                nuevoPunto = (nuevaX, nuevaY)

                if nuevoPunto not in puntosLlegada:             # Optimizacion para no considerar el mismo punto mas de una vez
                    puntosLlegada.append(nuevoPunto)

    return puntosLlegada


def cantidadMovimientos(puntoInicial, puntoFinal, tablero):
    posActual = [puntoInicial]                              # Nos damos un punto de partida
    cantMov = 0

    while not puntoFinal in posActual:
        posActual = posiblesMovimientos(posActual, tablero) # Se actualiza la posicion actual
        cantMov += 1

    return cantMov


def crearMatDistancias(puntos, tablero):
    matriz = list()

    # Calculamos la distancia entre todo par de puntos
    for p1 in puntos:
        fila = list()

        for p2 in puntos:
            dist = cantidadMovimientos(p1, p2, tablero)
            fila.append(dist)

        matriz.append(fila)

    return matriz


def generarCombinaciones(conjunto: list) -> list:

    # Funcion recursiva que dado un conjunto de puntos genera
    # todas sus posibles combinaciones (permutaciones?)

    combs = list()

    if len(conjunto) == 0:
        return [[]]
    
    for i in range(len(conjunto)):
        conjunto2 = conjunto.copy()
        elemento = conjunto2.pop(i)

        for c in generarCombinaciones(conjunto2):
            c.append(elemento)
            combs.append(c)

    return combs


def caminoMasCorto(puntos, tablero):
    matrizDistancias = crearMatDistancias(puntos, tablero)      # Tabla de distancias
    puntosParaCombinar = list(range(len(puntos)))               # [0, 1, 2, 3, ... , n]
    combinaciones = generarCombinaciones(puntosParaCombinar)    # Posibles combinaciones de [0, 1, ... , n]

    posiblesCostos = list()

    # Calcular distancias de las posibles combinaciones
    for c in combinaciones:
        costo = 0

        for i in range(len(c) - 1):
            p1 = c[i]
            p2 = c[i + 1]
            costo += matrizDistancias[p1][p2]

        costo += matrizDistancias[c[-1]][c[0]]
        posiblesCostos.append(costo)

    # Encontrar minimo de las distancias
    minimo = posiblesCostos[0]      # Necesito que minimo valga algo

    for costo in posiblesCostos:
        if costo < minimo:
            minimo = costo

    return minimo


def generarCaso():
    print("")
    tamanoTablero = int(input("Tamaño del tablero: "))
    cantidadCeldas = int(input("Cantidad de celdas especiales: "))

    if tamanoTablero < 4:
        print("Error, el tablero debe tener un tamaño mínimo de 4 celdas por lado")
        return                          # La ejecucion del caso termina si se ingresan datas erroneos

    if tamanoTablero > 1000:
        print("Error, el tablero debe tener un tamaño máximo de 1000 celdas por lado")
        return                          # Termina ejecucion
    
    if cantidadCeldas < 1 or cantidadCeldas > 16:
        print("Error, cantidad de celdas debe estar entre 1 y 16")
        return                          # Termina ejecucion

    # Generacion de Celdas Especiales
    celdasEspeciales = list()
    for j in range(cantidadCeldas):

        print("")
        print(f"Celda especial {j + 1}:")
        
        x = int(input("Coordenada x: "))
        y = int(input("Coordenada y: "))

        if not esPosicionValida(x, y, tamanoTablero):
            print(f"Error, las coordenadas de la celda especial {j + 1} está fuera de rango")
            return                      # Termina ejecucion

        celdasEspeciales.append((x, y)) # Par ordenado

    print("")

    # Aqui ocurre la magia
    movimientos = caminoMasCorto(celdasEspeciales, tamanoTablero)
    print(f"{movimientos} movimientos")



# PARTE PRINCIPAL DEL PROGRAMA
# Aca inicia la ejecucion del porgrama

# Pedir Cantidad de Casos y Validar
cantidadCasos = int(input("Cantidad de casos: "))
while cantidadCasos < 1 or cantidadCasos > 100:
    cantidadCasos = int(input("Cantidad de casos: "))

# Generar casos
for _ in range(cantidadCasos):
    generarCaso()
