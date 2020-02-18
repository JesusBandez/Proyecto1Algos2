import statistics
import math
import sys
import random
sys.setrecursionlimit(30000)

# Insertion Sort
def insertionsort(A:list) -> "void":
	"""Recorre el arreglo bucando un valor
	en el arreglo y posicionandolo en donde debe ir
	
	A: Arreglo a ordenar
	"""
	for j in range(1, len(A)):

		key = A[j]
		i = j - 1

		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1

		A[i+1] = key

def insertionsortIndex(A:list, p:int, r:int) -> "void":
	"""Version modificada de Insertion Sort la cual solo ordena
	el subarreglo de A que inicie en la posicion p y termine en
	la posicion f. Luego, se inserta el subarreglo ordenado en 
	el arreglo original	

	A: Arreglo a ordenar
	p: Primer elemento del subarreglo
	r: Ultimo elemento del subarreglo
	
	"""
	for i in range(p + 1, r + 1):
		
		key = A[i]
		j = i - 1

		while j >= p and key < A[j]:
			A[j+1] = A[j]
			j = j - 1
		A[j+1] = key

# Merge Sort
def mergesort(T:list) -> "void":
	""" Algoritmo que divide un arreglo a la mitad para ordenarlo.
	En caso de llegar a un subarreglo con pocos elementos, se aplica
	insertion sort para ordenar ese sub arreglo"""

	if len(T) <= 32:
		insertionsort(T)

	else:
		U = T[0:len(T)//2]
		V = T[len(T)//2:len(T)]
		mergesort(U)
		mergesort(V)
		merge(U, V, T)

def merge(U:list, V:list, T:list) -> "void":
	"""Procedimiento que une a dos arreglos ordenados en 
	otro arreglo ordenado
	
	U: arreglo ordenado del que se extraen los elementos
	V: arreglo ordenado del que se extraen los elementos
	T: arreglo ordenado con los elementos de U y V
	"""

	infinite = float("inf")
	i, j = 0, 0
	U.append(infinite)
	V.append(infinite)

	for k in range(0, len(U) + len(V)-2):
		if U[i] < V[j]:
			T[k] = U[i]
			i = i + 1
		else:
			T[k] = V[j]
			j = j + 1

# Quick Sort Iterativo
def quicksortIterative(A:list) -> "void":
	"""Version iterativa del Quick Sort
	
	A: Arreglo a ordenar
	"""

	N = len(A)
	n, m = 0, 1
	while m < N:
		n,m = n + 1, m * 2
	x = [0] * n
	y = [0] * n
	k, p, q = 0, 0, N
	while k != 0 or q-p >= 2:
		if q - p <= 1:
			k = k - 1
			p, q = x[k], y[k]
		elif q - p >= 2:
			z = A[(p+q)//2]
			r, w, b = p, p, q
			while w != b:
				if A[w] < z:
					A[r], A[w] = A[w], A[r]
					r, w = r + 1, w + 1
				elif A[w] == z:
					w = w + 1
				elif A[w] > z:
					b = b - 1
					A[b], A[w] = A[w], A[b]
			if r-p <= q - w:
				x[k] = w
				y[k] = q
				q = r
			elif q - w <= r - p:
				x[k] = p
				y[k] = r
				p = w
			k = k + 1

# Quick Sort Simple
def quicksortSimple(A:list, p:int, r:int) -> "void":
	""" Algoritmo que ordena un arreglo por medio de "pivotes"
	El ultimo elemento del arreglo a ordenar es usado como pivote"""

	tamanoSecuencia = r - p + 1

	if tamanoSecuencia <= 32 and p < r:	
		insertionsortIndex(A, p, r)


	elif tamanoSecuencia > 32 and p < r:
		q = partition(A, p, r)	
		quicksortSimple(A, p, q-1)
		quicksortSimple(A, q+1, r)

	# Para usarse se llama: quickSort(arreglo, 0, len(arreglo) - 1)

def partition(A:list, p:int, r:int) -> int:
	""" Funcion que posiciona los elementos en el arreglo
	segun sean mayores o menores que el pivote elegido.
	El pivote se elige como el ultimo elemento de arreglo

	A: Arreglo a ordenar
	p: Posicion del primero elemento del arreglo
	r: Posicion del ultimo elemento del arreglo
	"""

	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	return i + 1

# Median-of-three Quicksort
def medianOf3Quicksort(A:list, f:int, b:int) -> "void":
	""" Version de Quicksort que toma como pivote a la mediana
	de tres elementos del arreglo

	A: arreglo a ordenar
	f: Primera posicion del arreglo
	b: Primera posicion mas alla de la ultima posicion del arreglo
	"""

	quicksortLoop(A, f, b)
	insertionsortIndex(A, f, b-1)
	# Debe llamarse la primera vez con:
	# MedianOf3Quicksort(A, 0, len(A))

def quicksortLoop(A:list, f:int, b:int) -> "void":

	while (b-f > 32):

		medianOf3 = statistics.median([A[f], A[f + (b-f)//2], A[b-1]])
		p = partitionMedianOf3(A, f, b, medianOf3)
	
		if (p - f) >= (b - p):
			quicksortLoop(A, p, b)
			b = p - 1
		else:
			quicksortLoop(A, f, p)
			f = p + 1

def partitionMedianOf3(A:list, p:int, r:int, x:int) -> int:
	i = p - 1
	j = r
	while True:
		while True:
			j = j - 1
			if A[j]<=x:
				break

		while True:
			i = i + 1
			if A[i]>=x:
				break
		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j

# Dual Pivot Quicksort
def dualPivotQuicksort(A:list, left:int, right:int) -> "void":
	""" Version de Quicksort la cual usa dos pivotes

	A: Arreglo a ordenar
	left: Primera posicion del arreglo
	right: Ultima posicion del arreglo

	"""

	if right - left <= 32:		
		insertionsortIndex(A, left, right)
	else:
		if A[left] > A[right]:
			p, q = A[right], A[left]
		else:
			p, q = A[left], A[right]
		l, g = left + 1, right - 1
		k = l

		while k <= g:
			if A[k] < p:
				A[k], A[l] = A[l], A[k]
				l = l + 1
			else:
				if A[k] >= q:

					while A[g] > q and k < g:
						g = g - 1

					if A[g] >= p:
						A[k], A[g] = A[g], A[k]
					else:
						A[k], A[g] = A[g], A[k]
						A[k], A[l] = A[l], A[k]
						l = l + 1

					g = g - 1					
			k = k + 1

		l = l - 1
		g = g + 1
		A[left] = A[l]
		A[l] = p
		A[right] = A[g]
		A[g] = q
		dualPivotQuicksort(A, left, l-1)
		dualPivotQuicksort(A, l+1, g-1)
		dualPivotQuicksort(A, g+1, right)

		# Debe llamarse con: dualPivotQuicksort(A, 0, len(A)-1)

# Intro Sort
def introsort(A:list, f:int, b:int) -> 'void':
	"""
	INPUTS:

		A: Una estructura de datos de acceso aleatorio
	que contiene la secuencia de datos a ordenar en las
	posiciones A[f]...A[b-1]

		f: la primera posición de la secuencia

		b: la primera posición despues del final de la
	secuencia

	OUTPUT:
			A es permutada y puesta en orden creciente
			tal que A[f]<=A[f+1]<=...<=A[b-1]"""

	depthLimit = 2 * int( math.floor( math.log(b-f, 2) ) )
	introsortLoop(A, f, b, depthLimit)
	insertionsortIndex(A, f, b - 1)

	# Se llama con: introsort(A, 0, len(A))

def maxHeapify(A:list, i:int, heapSize:int) -> 'void':
	""" Dado el arrelo A, el indice i y el tamaño del Heap
	se permuta A de tal modo que A[i] constituya un nodo del
	maxheap 
	"""
	l = 2*i + 1;
	r = 2*i + 2;

	if l < heapSize and A[i] < A[l]:
		largest = l;

	else:
		largest = i;

	if r < heapSize and A[largest] < A[r]:
		largest = r;

	if largest != i:
		#intercambio A[i] y A[largest]
		A[i], A[largest] = A[largest], A[i];
		maxHeapify(A, largest, heapSize)

def buildMaxHeapIndex(A:list, f:int, b:int) -> 'void':
	"""Variante de Build_Max_Heap. Convierte el arreglo A en
	un Max-Heap en el intervalo [f,b) donde 0<=f<b<len(A)
	"""

	H = (b//2) - 1;

	for i in range(H, f-1,-1):
		maxHeapify(A, i, b);

def heapsortIndex(A:list, f:int, b:int) -> 'void':
	""" Variante del Algoritmo de Ordenación Heapsort.
	Ordena al arreglo A en el intervalo [f,b) donde
	0<=f<b<len(A)
	
	INPUTS:

		A: Una estructura de datos de acceso aleatorio
	que contiene la secuencia de datos a ordenar en las
	posiciones A[f]...A[b-1]

		f: la primera posición de la secuencia

		b: la primera posición despues del final de la
	secuencia

	OUTPUT:
			A es permutada y puesta en orden creciente
			tal que A[f]<=A[f+1]<=...<=A[b-1]

	"""

	buildMaxHeapIndex(A, f, b);
	heapSize = b;

	while heapSize > f+1:
		#intercambio el primero y el ultimo elemento
		A[f], A[heapSize - 1] = A[heapSize - 1], A[f];
		heapSize = heapSize - 1;
		maxHeapify(A, f, heapSize);

def introsortLoop(A:list, f:int, b:int, depthLimit:int) -> 'void':
	"""
	INPUTS:

		A,f y b como en Introsort;

		depthLimit: Entero no negativo

	OUTPUT:
			A es permutada tal que A[i]<=A[j]
			para todo f<=i<j<b y sizeThreshold < j-i"""

	sizeThreshold = 32

	while (b-f > sizeThreshold):

		if depthLimit == 0:
			heapsortIndex(A, f, b)
			return

		medianOf3 = statistics.median([A[f], A[f + (b-f)//2], A[b-1]])
		depthLimit = depthLimit - 1
		p = partitionMedianOf3(A, f, b, medianOf3)
		introsortLoop(A, p, b, depthLimit)
		b = p

# Timsort
def timsort(arr:list) -> list:
	"""Timsort utiliza el principio de mergesort, pero inicialmente ordena
	subarreglos de tamaño minrun = 32 con insertionsort y ejecuta
	merge para unir subarreglos contiguos en otro subarreglo de mayor tamaño 
	ordenado, hasta ordenar la estructura completa

	INPUTS:

		A: Estructura de datos a ordenar

	OUTPUT:
			A es permutada tal que A[i]<=A[j]
			para todo l<=i<j<=r """

	minrun = 32
	n = len(arr)

	for start in range(0, n, minrun):
		end = min(start + minrun - 1, n - 1)
		insertionsortIndex(arr, start, end)

	currSize = minrun

	while currSize < n:    
		
		for start in range(0, n, currSize * 2):
			mid = min(n - 1, start + currSize - 1)
			end = min(n - 1, mid + currSize)
			arr = mergeIndex(arr, start, mid, end)
		currSize = currSize * 2

	return arr

def mergeIndex(arr:list, start:int, mid:int, end:int) -> list:
	"""Dados dos subarreglos ordenados y contiguos [start,mid]
	y [mid+1, end] se ordena el intervalo [start,end] 


	INPUTS:

		arr: Estructura de datos a ordenar
		star: indice de la primera posicion a ordenar
		mid: indice de la ultima posición del primer subarreglo
		end: indice de la ultima posición del segundo subarreglo

	OUTPUT:
			A es permutada tal que A[i]<=A[j]
			para todo l<=i<j<=r """

	if (mid == end):
		return arr

	first = arr[start:mid+1]
	last = arr[mid+1:end+1]
	len1 = mid - start+1
	len2 = end - mid
	ind1 = 0
	ind2 = 0
	ind  = start
     
	while (ind1 < len1 and ind2 < len2):

		if (first[ind1] < last[ind2]):
			arr[ind] = first[ind1]
			ind1 = ind1 + 1

		else:
			arr[ind] = last[ind2]
			ind2 = ind2 + 1
		ind = ind + 1

	while (ind1 < len1):
		arr[ind] = first[ind1]
		ind1 = ind1 + 1
		ind = ind + 1
              
	while (ind2 < len2):
		arr[ind] = last[ind2]
		ind2 = ind2 + 1
		ind = ind + 1

	return arr

# Quicksort with 3 Way Partitioning
def quicksortWith3WayPartitioning(A:list, l:int, r:int) -> 'void':
	"""Quicksort particionando en tres, con insertionsort
	para ordenar los subarreglos de tamaño menor o igual a 32

	INPUTS:

		A: Estructura de datos a ordenar
		l: indice de la primera posicion a ordenar
		r: indice de la ultima posición a ordenar

	OUTPUT:
			A es permutada tal que A[i]<=A[j]
			para todo l<=i<j<=r """

	i, p = l-1, l - 1
	j, q = r, r
	v = A[r]

	if(r <= l):
		return

	while True:

		i = i + 1
		while (A[i] < v):
			i = i+1
		assert(A[i] >= v)

		j = j - 1
		while v < A[j]:

			if (j == l):
				break
			j = j - 1
		assert(A[j] <= v or j == l)

		if (i >= j):
			break

		assert(A[i] >= A[j] and i < j)

		A[i], A[j] = A[j], A[i]
		
		assert(A[i] <= A[j] and i < j)

		if (A[i] == v):
			# Coloco A[i] al en el sub arreglo ordenado [l,p]
			p = p + 1
			A[p], A[i] = A[i], A[p]

		if (v == A[j]):
			# Coloco A[j] al en el sub arreglo ordenado [q,r]
			q = q - 1
			A[q], A[j] = A[j], A[q]

	A[i], A[r] = A[r], A[i]
	j = i - 1
	i = i + 1

	for k in range(l,p):
		A[k], A[j] = A[j], A[k]
		j = j - 1

	for k in range(r-1,q,-1):
		A[i], A[k] = A[k], A[i]
		i = i + 1

	# Usamos Insertion si los subarreglos son menores o iguales a 32
	if l<j and j-l<=32:
		insertionsortIndex(A,l,j)

	if i < r and r-i<=32:
		insertionsortIndex(A,i,r)
	 
	
	quicksortWith3WayPartitioning(A,l,j)
	quicksortWith3WayPartitioning(A,i,r)

	# Debe llamarse con quicksortWith3WayPartitioning(A, 0, len(A) - 1)


