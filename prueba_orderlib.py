import sys
import argparse # Usada para introducir los argumentos al llamar al programa
import graficar_puntos as gp 
import statistics
from orderlib import *
from random import randint, uniform
from time import time # Usada para calcular el tiempo de ejecucion

sys.setrecursionlimit(10000000) # Aumenta la profundidad maxima de las recursiones


def leerArgumentos() -> "void":
	""" Procedimiento que permite ingresar los argumentos al programa
	"""
	# Permite introducir los argumentos
	argumentos = argparse.ArgumentParser()
	argumentos.add_argument("secuencia", help = "Cantidad de elementos",
		type = int, nargs="*", default = [1000])
	argumentos.add_argument("-i", help = "Numero de intentos de cada prueba",
		type = int, default = 3)
	argumentos.add_argument("-t", help = "Tipo de prueba que se realizara", 
		type = int, default = 1)
	argumentos.add_argument("-g", help = "Muestra una grafica comparativa",
		action="store_const", default=False, const=True)
	
	argumentos = argumentos.parse_args()
	
	return argumentos

def comprobarArgumentos(A:[int], 
	i:int, t:int, g:bool,) -> "void":
	""" Procedimiento para comprobar que los argumentos ingresados son correctos

	A: Secuencia ingresada por el usuario
	i: Cantidad de veces que se debe repetir una prueba de tamano A[i]
	t: Tipo de prueba a realizar sobre los algoritmos
	g: El programa muestra una grafica con los resultados
	"""

	try: 
		assert(all(A[i] >= 0 for i in range(0,len(A))))			
	except:
		print("\nLos argumentos ingresados no son validos:")
		print("La secuencia solo debe tener elementos mayores o iguales que 0")		
		exit()

	try:
		assert(i > 0)
	except:
		print("\nLos argumentos ingresados no son validos:")
		print("El argumento i debe ser mayor que 0")

	try:
		assert(1 <= t <= 7)
	except:
		print("\nLos argumentos ingresados no son validos:")
		print("El argumento t debe estar entre 1 y 7, incluyendo los extremos")

	try:
		assert(g == False or len(A) != 1)
	except:
		print("Si quiere una grafica, debe ingresar al menos 2 elementos en la secuencia")
		exit()

def nombrarAlgoritmos() -> [str]:
	""" Funcion que devuelve una lista con los nombres de los algoritmos
	dentro de un arreglo	
	"""

	nombresAlgoritmos = ["Mergesort", "Quicksort iterativo",
		"Quicksort simple", "Median-of-3 quicksort", "Introsort", 
		"Quicksort with 3-way partitioning", "Dual pivot Quicksort",
		"Timsort"]

	return nombresAlgoritmos

def generarArreglo(n:int, t:int) -> [int]: # MODIFICAR!!!!!!!!!!!!!!!!!!
	""" Genera un arreglo de tamaño n, este arreglo tiene elementos
	y ordenes distintos que dependen del parametro t
	
	n: Numero de elementos con los que se genera el arreglo
	t: Parametro que modifica los elementos del arreglo y su orden
	"""

	if t == 1: # Numeros reales entre 0 y 1, sin incluir 1
		arreglo = [uniform(0,1) for i in range(0,n)]

	elif t == 2 or t == 6 or t == 7: # Numeros enteros ordenados de forma ascendente
		############# ES POSIBLE QUE ESTO NO SEA CORRECTO 
		arreglo = [randint(0,n) for i in range(0,n)]
		arreglo.sort()

	elif t == 3: # Numeros enteros ordenados de forma descendente
		############# ES POSIBLE QUE ESTO NO SEA CORRECTO
		arreglo = [randint(0,n) for i in range(0,n)]
		arreglo.sort(reverse=True)

	elif t == 4: # Ceros y unos generados aleatoriamente
		arreglo = [randint(0,1) for i in range(0,n)]

	elif t == 5:
		# Secuencia de la forma:
		# [1, 2, ... , n/2, n/2, ..., 2, 1]
		# Es esa division la division entera???
		##############

		arreglo = []
		k = 1

		while k <= n // 2:
			arreglo.append(k)
			k = k + 1

		k = n // 2
		while k >= 1:
			arreglo.append(k)
			k = k - 1

	if t == 6:
		# Realmente puedo usar como arreglo base el arreglo tipo 2?
		# Por la forma en la que lo describe, es OBLIGATORIO que 
		# n > 8

		i = 0
		while i < 16:
			q = randint(0, len(arreglo)- 9)
			p = q + 8
			arreglo[q], arreglo[p] = arreglo[p], arreglo[q]
			i = i + 1

	elif t == 7:
		# Mismas preguntas que la tipo 6 pero con n > 4
		# n / 4 es la division entera?

		i = 0
		while i <= n // 4:
			q = randint(0, len(arreglo)- 5)
			p = q + 4
			arreglo[q], arreglo[p] = arreglo[p], arreglo[q]
			i = i + 1

	return arreglo

def obtenerTiempos(A:[int], C:[[int]]) -> "void":
	""" Procedimiento para medir el tiempo de ejecucion de los algoritmos	

	A: arreglo que los algoritmos deben ordenar
	C: arreglo para guardar los tiempos de cada algoritmo	
	"""

	# Crear copia del arreglo prueba
	copiaArregloPrueba = A[:]

	# Medida de tiempo para Merge sort
	tiempoInicial = time()
	mergesort(A)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[0].append(tiempoEjecucion)

	# Medida de tiempo para Quicksort iterativo
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	quicksortIterative(A)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[1].append(tiempoEjecucion)

	# Medida de tiempo para Quicksort simple
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	quicksortSimple(A, 0, len(A) - 1)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[2].append(tiempoEjecucion)

	# Medida de tiempo para Median-of-3 quicksort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	#################################medianOf3Quicksort(A, 0, len(A))
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[3].append(tiempoEjecucion)

	# Medida de tiempo para Introsort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	################################### Introsort(A) ################
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[4].append(tiempoEjecucion)

	# Medida de tiempo para Quicksort with 3-way partitioning
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	################################## quicksortWith3-wayPartitioning(A)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[5].append(tiempoEjecucion)

	# Medida de tiempo para Dual pivot Quicksort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	dualPivotQuicksort(A, 0, len(A) - 1)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[6].append(tiempoEjecucion)

	# Medida de tiempo para Timsort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	###################################### Timsort() #############
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	C[7].append(tiempoEjecucion)

def promedios(A:[[int]], B:[int]) -> "void":
	""" Procedimiento para calcular el promedio de los arreglos dentro del
	arreglo A

	A: Arreglo de arreglos que contiene los tiempos de las ejecuciones
		de los algoritmos
	B: Arreglo que guarda los promedios
	"""

	j = 0
	for arreglo in A:
		B[j] = statistics.mean(arreglo)
		j = j + 1

def desviacionesEstandar(A:[[int]], B:[int]) -> "void":
	""" Procedimiento para calcular las desviaciones de los arreglos dentro
	del arreglo A

	A: Arreglo de arreglos que contiene los tiempos de las ejecuciones
		de los algoritmos
	B: Arreglo que guarda las desviaciones estandar	
	"""

	j = 0
	for arreglo in A:
		B[j] = statistics.stdev(arreglo)
		j = j + 1

def redondear(A:[int]) -> "void":
	""" Procedimiento que redondea a dos decimales todos los elementos dentro
	del arreglo A
	
	A: Arreglo de numeros reales que se redondearan a dos decimales
	"""

	for i in range(0,len(A)):
		A[i] = round(A[i], 2)

def imprimirValoresFinales(A:[int], B:[int], 
	C:[str], n:int) -> "void":
	""" Imprime los valores de los arreglos A, B y C bajo una plantilla

	A: Arreglo con los promedios de los algoritmos
	B: Arreglo con las desviaciones de los algoritmos
	C: Arreglo que contiene los nombres de los algoritmos
	n: Cantidad de elementos que contenia el arreglo ordenado
	"""

	print("\n\nArreglo de: " + str(n) + " elementos", end="")

	for i in range(0, len(A)):
		print("\nTiempo promedio de " + C[i] + " " + str(A[i]) + " sg, " 
			+ str(B[i]) + " std")

def dibujarGrafica(secuencia:[int], tiempos:[[int]], 
	nombres:[str]) -> "void":
	"""Procedimiento usado para dibujar la grafica con los resultados de los 
	tiempos de ejecucion de los algoritmos
	
	secuencia: Arreglo que contiene la cantidad de elementos que tuvo
		cada arreglo con los que se hicieron las pruebas
	tiempos: Arreglo de arreglos con todos los tiempos promedios de los 
		algoritmos
	nombres: Arreglo con los nombres de los algoritmos
	"""

	if __name__ == '__main__':		
		
		i = 0
		while i < len(nombres):
			tiempoAlgo = [tiempos[j][i] for j in range(0,len(secuencia))]				
			gp.dibujar_grafica(secuencia, tiempoAlgo, nombres[i])
			i = i + 1	

		gp.mostrar_grafico("Tiempo (seg)", "Número de elementos")

# Lee los argumentos del programa
argumentos = leerArgumentos()

# Simplifica el nombre de los argumentos para el resto del programa
secuencia = argumentos.secuencia
i = argumentos.i
t = argumentos.t
g = argumentos.g

# Verficar que los argumentos tiene valores validos
comprobarArgumentos(secuencia, i, t, g)

# Lista con los nombres de los algoritmos
nombresAlgoritmos = nombrarAlgoritmos()

# Guarda los tiempos promedio finales de cada secuencia[i] elementos
tiemposTotales = []

# Itera el tamaño del arreglo prueba por los elementos de la secuencia 
# introducida por el usuario
for n in secuencia:

	# Arreglo que guardara los tiempos de cada algoritmo al ejecutarse
	tiempos = [[] for i in range(0,8)]

	k = 0
	while k < i: # Repetir las pruebas por el numero de intentos ingresados

		arregloPrueba = generarArreglo(n,t) # Crea el arreglo de prueba

		# Toma el tiempo a los algoritmos
		obtenerTiempos(arregloPrueba, tiempos)

		k = k + 1

	# Calculo de promedios y desviaciones
	# Arreglo que guardara los promedios de cada algoritmo
	tiemposPromedio = [0 for i in range(0,8)]

	# Arreglo que guardaran las desviaciones de cada algoritmo
	desviaciones = [0 for i in range(0,8)]

	# Calcular promedios y desviaciones
	promedios(tiempos, tiemposPromedio)
	desviacionesEstandar(tiempos, desviaciones)

	# Redondear a dos decimales los promedios y las desviaciones
	redondear(tiemposPromedio)
	redondear(desviaciones)

	# Imprimir valores finales		
	imprimirValoresFinales(tiemposPromedio, 
		desviaciones, nombresAlgoritmos, n)

	# Guardar los tiempos promedios finales de cada secuencia[i] elementos
	tiemposTotales.append(tiemposPromedio)

# Mostrar grafica si fue solicitada en los argumentos
if g:
	dibujarGrafica(secuencia, tiemposTotales, 
		nombresAlgoritmos)
