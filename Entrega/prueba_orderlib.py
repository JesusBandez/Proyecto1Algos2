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

	# Precondicion
	assert(True)

	# Permite introducir los argumentos
	argumentos = argparse.ArgumentParser()
	argumentos.add_argument("secuencia", help = "Cantidad de elementos",
		type = int, nargs="*")
	argumentos.add_argument("-i", help = "Numero de intentos de cada prueba",
		type = int, default = 3)
	argumentos.add_argument("-t", help = "Tipo de prueba que se realizara", 
		type = int, default = 1)
	argumentos.add_argument("-g", help = "Muestra una grafica comparativa",
		action="store_const", default=False, const=True)
	
	argumentos = argumentos.parse_args()

	# Postcondicion
	assert(True)
	
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
		assert(A != [])
	except:
		print("Debe ingresar al menos una secuencia con un elemento")
		exit()

	try: 
		assert(all(A[i] > 0 for i in range(0,len(A))))			
	except:
		print("\nLos argumentos ingresados no son validos:")
		print("La secuencia solo debe tener elementos mayores que 0")		
		exit()

	try:
		assert(i > 0)
	except:
		print("\nLos argumentos ingresados no son validos:")
		print("El argumento i debe ser mayor que 0")
		exit()

	try:
		assert(1 <= t <= 7)
	except:
		print("\nLos argumentos ingresados no son validos:")
		print("El argumento t debe estar entre 1 y 7, incluyendo los extremos")
		exit()

	try:
		assert(g == False or len(A) != 1)
	except:
		print("Si quiere una grafica, debe ingresar al menos 2 elementos en la secuencia")
		exit()

def nombrarAlgoritmos() -> [str]:
	""" Funcion que devuelve una lista con los nombres de los algoritmos
	dentro de un arreglo	
	"""

	# Precondicion
	assert(True)

	nombresAlgoritmos = ["Mergesort", "Quicksort iterativo",
		"Quicksort simple", "Median-of-3 quicksort", "Introsort", 
		"Quicksort with 3-way partitioning", "Dual pivot Quicksort",
		"Timsort"]

	#Postcondicion
	assert(nombresAlgoritmos != [])

	return nombresAlgoritmos

def generarArreglo(n:int, t:int) -> list:
	""" Genera un arreglo de tamaño n, este arreglo tiene elementos
	y ordenes distintos que dependen del parametro t
	
	n: Numero de elementos con los que se genera el arreglo
	t: Parametro que modifica los elementos del arreglo y su orden
	"""

	# Precondicion
	assert(n > 0 and 1 <= t <= 7)

	if t == 1: # Numeros reales entre 0 y 1, sin incluir 1
		arreglo = [uniform(0,1) for i in range(0,n)]

	elif t == 2 or t == 6 or t == 7: # Numeros enteros ordenados de forma ascendente		
		arreglo = [randint(0,n) for i in range(0,n)]
		arreglo.sort()

	elif t == 3: # Numeros enteros ordenados de forma descendente		
		arreglo = [randint(0,n) for i in range(0,n)]
		arreglo.sort(reverse=True)

	elif t == 4: # Ceros y unos generados aleatoriamente
		arreglo = [randint(0,1) for i in range(0,n)]

	elif t == 5:
		# Secuencia de la forma: [1, 2, ... , n/2, n/2, ..., 2, 1]
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
		# Arreglo de enteros ordenados al que se le intercambian
		# dos elementos separados por otros 8 elementos 16 veces
		if n > 8:
			# Solo es posible si la secuencia tiene mas de 8 elementos
			i = 0
			while i < 16:
				q = randint(0, len(arreglo)- 9)
				p = q + 8
				arreglo[q], arreglo[p] = arreglo[p], arreglo[q]
				i = i + 1

	elif t == 7:
		# Arreglo de enteros ordenados al que se le intercambian
		# dos elementos separados por otros 4 elementos n/4 veces
		if n > 4:
			# Solo es posible si la secuencia tiene mas de 4 elementos
			i = 0
			while i <= n // 4:
				q = randint(0, len(arreglo)- 5)
				p = q + 4
				arreglo[q], arreglo[p] = arreglo[p], arreglo[q]
				i = i + 1

	# Postcondicion
	assert( (t != 1 or all(0 <= arreglo[i] < 1 for i in range(0, len(arreglo))))
		or (t != 2 or all(arreglo[i] <= arreglo[i + 1] for i in range(0, len(arreglo)-1)))
		or (t != 3 or all(arreglo[i] >= arreglo[i + 1] for i in range(0, len(arreglo)-1)))
		or (t != 4 or all((arreglo[i] == 0 or arreglo[i] == 1) for i in range(0, len(arreglo))))
		or (t != 5 or all(arreglo[i] <= arreglo[i + 1] for i in range(0, len(arreglo)-1)) or
			any(arreglo[i] > arreglo[i + 1] for i in range(0, len(arreglo)-1)))
		or (t != 6 or all(arreglo[i] <= arreglo[i + 1] for i in range(0, len(arreglo)-1)) or
			any(arreglo[i] > arreglo[i + 1] for i in range(0, len(arreglo)-1)))		)


	return arreglo

def obtenerTiempos(A:list, C:[[float]]) -> "void":
	""" Procedimiento para medir el tiempo de ejecucion de los algoritmos	

	A: arreglo que los algoritmos deben ordenar
	C: arreglo para guardar los tiempos de cada algoritmo	
	"""

	# Precondicion
	assert( A != [] and all(all(C[i][j]>=0 for j in range(0, len(C[i]))) 
		for i in range(0, 8)))

	# Crear copia del arreglo prueba
	copiaArregloPrueba = A[:]

	# Medida de tiempo para Merge sort
	tiempoInicial = time()
	mergesort(A)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[0].append(tiempoEjecucion)

	# Medida de tiempo para Quicksort iterativo
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	quicksortIterative(A)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[1].append(tiempoEjecucion)

	# Medida de tiempo para Quicksort simple
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	quicksortSimple(A, 0, len(A) - 1)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[2].append(tiempoEjecucion)

	# Medida de tiempo para Median-of-3 quicksort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	medianOf3Quicksort(A, 0, len(A))
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[3].append(tiempoEjecucion)

	# Medida de tiempo para Introsort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	introsort(A, 0, len(A))
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[4].append(tiempoEjecucion)

	# Medida de tiempo para Quicksort with 3-way partitioning
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	quicksortWith3WayPartitioning(A, 0, len(A) - 1)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[5].append(tiempoEjecucion)

	# Medida de tiempo para Dual pivot Quicksort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	dualPivotQuicksort(A, 0, len(A) - 1)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[6].append(tiempoEjecucion)

	# Medida de tiempo para Timsort
	A = copiaArregloPrueba[:]
	tiempoInicial = time()
	timsort(A)
	tiempoFinal = time()
	tiempoEjecucion = tiempoFinal - tiempoInicial
	comprobarOrden(A)
	C[7].append(tiempoEjecucion)

	# Postcondicion
	assert(all(all(C[i][j]>=0 for j in range(0, len(C[i]))) for i in range(0, 8)))

def comprobarOrden(A:list) -> "void":
	""" Procedimiento para comprobar que el arreglo que se pasa
	como argumento esta ordenado

	A: Arreglo ordenado
	"""
	assert(all(A[i] <= A[i+1] for i in range(0,len(A)-1)))

def promedios(A:[[float]], B:[float]) -> "void":
	""" Procedimiento para calcular el promedio de los arreglos dentro del
	arreglo A

	A: Arreglo de arreglos que contiene los tiempos de las ejecuciones
		de los algoritmos
	B: Arreglo que guarda los promedios
	"""

	# Precondicion
	assert(all(A[i] != [] for i in range(0, 8)) and 
		all(B[i] == 0 for i in range(0, 8)))

	j = 0
	for arreglo in A:
		B[j] = statistics.mean(arreglo)
		j = j + 1

	# Postcondicion
	assert(all(B[i] == statistics.mean(A[i]) for i in range(0, 8)))

def desviacionesEstandar(A:[[float]], B:[float]) -> "void":
	""" Procedimiento para calcular las desviaciones de los arreglos dentro
	del arreglo A

	A: Arreglo de arreglos que contiene los tiempos de las ejecuciones
		de los algoritmos
	B: Arreglo que guarda las desviaciones estandar	
	"""

	# Precondicion
	assert(all(A[i] != [] for i in range(0, 8)) and 
		all(B[i] == 0 for i in range(0, 8)))

	j = 0
	for arreglo in A:
		B[j] = statistics.stdev(arreglo)
		j = j + 1

	# Postcondicion
	assert(all(B[i] == statistics.stdev(A[i]) for i in range(0, 8)))

def redondear(A:[float]) -> "void":
	""" Procedimiento que redondea a dos decimales todos los elementos dentro
	del arreglo A
	
	A: Arreglo de numeros reales que se redondearan a dos decimales
	"""

	# Precondicion
	assert(all(A[i]>= 0 for i in range(0, 8)))

	for i in range(0,len(A)):
		A[i] = round(A[i], 2)

	# Postcondicion
	assert(all(A[i]>= 0 for i in range(0, 8)))

def imprimirValoresFinales(A:[float], B:[float], 
	C:[str], n:int) -> "void":
	""" Imprime los valores de los arreglos A, B y C bajo una plantilla

	A: Arreglo con los promedios de los algoritmos
	B: Arreglo con las desviaciones de los algoritmos
	C: Arreglo que contiene los nombres de los algoritmos
	n: Cantidad de elementos que contenia el arreglo ordenado
	"""

	# Precondicion
	assert(all(A[i] >= 0 for i in range(0, 8)) 
		and all(B[i] >= 0 for i in range(0, 8))
		and C != [] and n > 0)

	print("\n\nArreglo de: " + str(n) + " elementos", end="")

	for i in range(0, len(A)):
		print("\nTiempo promedio de " + C[i] + " " + str(A[i]) + " sg, " 
			+ str(B[i]) + " std")

	# Postcondicion
	assert(all(A[i] >= 0 for i in range(0, 8)) 
		and all(B[i] >= 0 for i in range(0, 8))
		and C != [] and n > 0)

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

	# Precondicion
	assert(all(secuencia[i] > 0 for i in range(0, len(secuencia)))	
		and nombres != [])

	if __name__ == '__main__':		
		
		i = 0
		while i < len(nombres):
			tiempoAlgo = [tiempos[j][i] for j in range(0,len(secuencia))]				
			gp.dibujar_grafica(secuencia, tiempoAlgo, nombres[i])
			i = i + 1	

		gp.mostrar_grafico("Número de elementos", "Tiempo (seg)")

	# Postcondicion
	assert(all(secuencia[i] > 0 for i in range(0, len(secuencia)))
		and nombres != [])

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

	if i > 1:
		# Solo se calculan las desviaciones si se hicieron mas de
		# un intento o pruebas sobre cada algoritmo
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
