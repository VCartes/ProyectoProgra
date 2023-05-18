def esPosicionValida(x, y, tablero):
    if x > tablero or x < 1 or y > tablero or y < 1:
        return False
    return True


def posiblesMovimientos(puntosPartida, tablero):
    movimientos = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    puntosLlegada = list()

    for punto in puntosPartida:
        for mov in movimientos:
            nuevaX = punto[0] + mov[0]
            nuevaY = punto[1] + mov[1]

            if esPosicionValida(nuevaX, nuevaY, tablero):
                puntosLlegada.append((nuevaX, nuevaY))

    return puntosLlegada



def cantidadMovimientos(puntoInicial, puntoFinal, tablero):
    posActual = [(puntoInicial)]
    cantMov = 0

    while not puntoFinal in posActual:
        posActual = posiblesMovimientos(posActual, tablero)
        cantMov += 1

    return cantMov


def crearMatDistancias(puntos, tablero):
    matriz = list()

    for p1 in puntos:
        fila = list()
        for p2 in puntos:
            dist = cantidadMovimientos(p1, p2, tablero)
            fila.append(dist)

        matriz.append(fila)

    return matriz


def generarCombinaciones(conjunto: list) -> list:
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
    matrizDistancias = crearMatDistancias(puntos, tablero)
    puntosParaCombinar = list(range(len(puntos)))
    combinaciones = generarCombinaciones(puntosParaCombinar)

    posiblesCostos = list()

    for c in combinaciones:
        costo = 0

        for i in range(len(c) - 1):
            j = i + 1
            costo += matrizDistancias[i][j]

        costo += matrizDistancias[len(c) - 1][0]
        posiblesCostos.append(costo)

    minimo = posiblesCostos[0]

    for costo in posiblesCostos:
        if costo < minimo:
            minimo = costo

    return minimo


def generarCaso():
    tamanoTablero = int(input("Tamaño del tablero: "))
    cantidadCeldas = int(input("Cantidad de celdas especiales: "))

    if tamanoTablero < 4 or tamanoTablero > 1000:
        print("Error, valor debe estar entre 4 y 1000")
        return

    if cantidadCeldas < 1 or tamanoTablero > 16:
        print("Error, valor debe estar entre 1 y 16")
        return

    celdasEspeciales = list()
    for j in range(cantidadCeldas):
        print(f"Celda especial {j + 1}")
        x = int(input("Coordenada x: "))
        y = int(input("Coordenada y: "))

        if not esPosicionValida(x, y, tamanoTablero):
            print("Error, punto invalido")
            return

        celdasEspeciales.append((x, y))

    print(caminoMasCorto(celdasEspeciales, tamanoTablero))



cantidadCasos = int(input("Cantidad de casos: "))
while cantidadCasos < 1 or cantidadCasos > 100:
    cantidadCasos = int(input("Cantidad de casos: "))

for i in range(cantidadCasos):
    generarCaso()
