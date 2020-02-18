from orderlib import *
from random import *
def generarArreglo(n:int, t:int) -> [int]:
	""" Genera un arreglo de tamaño n, este arreglo tiene elementos
	y ordenes distintos que dependen del parametro t
	
	n: Numero de elementos con los que se genera el arreglo
	t: Parametro que modifica los elementos del arreglo y su orden
	"""

	if t % 2 == 1 and t != 7: # Los arreglo de tipo 1, 3 y 5 son reales del 0 al 1
		arreglo = [uniform(0,1) for i in range(0,n)]
	elif t % 2 == 0 and t != 7: # Los arreglos de tipo 2, 4 y 6 son enteros del 0 al n
		arreglo = [randint(0,n) for i in range(0,n)]
	
	if t == 3 or t == 4: # Los arreglos tipo 3 y 4 tienen orden creciente
		arreglo.sort()
	elif t == 5 or t == 6: # Los arreglos tipo 5 y 6 tienen orden decreciente
		arreglo.sort(reverse=True)

	if t == 7:
		arreglo = [randint(0,1) for i in range(0,n)]
	
	return arreglo

# Se generan 100 arreglos de enteros desordenados y se comprueba que el
# algoritmo usado los ordena
for i in range(0,2000):
	n = 2000
	t = 2
	arreglo = generarArreglo(n, t)	
	quickSortWith3WayPartitioning(arreglo, 0, len(arreglo) - 1)
	

	# Comprobar el orden: 
	assert(all(arreglo[i] <= arreglo[i+1] for i in range(0,len(arreglo)-1)))
	print(i+1)