Integrantes:
- Vicente René Cartes Cortés
- Alexis Andrés Sotomayor Saldivia
- Cristofer Luis Mamani Marino
- Guido Esteban Aravena Retamal


Instrucciones de Ejecución:

Para iniciar el programa, como este es un archivo .py, se puede correr desde la consola en Windows corriendo el comando "python .\ajedrez.py". También existen varias otras maneras de ejecutar un script de Python y todas ellas deberían funcionar de igual manera.

Al iniciar el programa, se pide al usuario que ingrese en una línea la cantidad de casos a ejecutar. Este valor debe ser un número entero entre 1 y 100 (incluyendo los extremos), si el valor está fuera de rango, se le pedirá al usuario que vuelva a ingresar el dato.

Después, se generará la cantidad de casos especificados. Para esto, se debe ingresar dos números enteros (cada uno en una línea), que representan el tamaño del tablero y la cantidad de celdas especiales. El tamaño del tablero debe ser mayor o igual a 4 y menor o igual a 1000. La cantidad de celdas especiales debe ser un número entero mayor o igual a 1 y menor o igual a 16. Si alguna de las condiciones especificadas no se cumple, la ejecución del caso actual termina y se empieza con el siguiente.

Posterior a esto, se ingresan las coordenadas x e y de las celdas especiales (cuya cantidad ya fue ingresada). Primero se le pide al usuario la coordenada x y en la siguiente línea la coordenada y. Ambas coordenadas deben estar dentro del tablero de ajedrez y si esto no se cumple, se descarta el caso actual y se prosigue al siguiente.

Una vez terminó el ingreso de datos para el caso actual, se busca el camino más corto y se despliega la cantidad de movimientos necesarios. Luego, se termina el caso actual y se ejecuta el siguiente.

Una vez fueron ejecutados todos los casos de prueba solicitados por el usuario, el programa termina su ejecución.
