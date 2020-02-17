import statistics 

# Insertion Sort
def insertionsort(A:[int]) -> "void":
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

def insertionsortIndex(A:[int], p:int, f:int) -> "void":
	"""Version modificada de Insertion Sort la cual solo ordena
	el subarreglo de A que inicie en la posicion p y termine en
	la posicion f. Luego, se inserta el subarreglo ordenado en 
	el arreglo original	

	A: Arreglo a ordenar
	p: Primer elemento del subarreglo
	f: Ultimo elemento del subarreglo
	
	"""
	
	B = A[p:f+1] # Conseguir subarreglo que se debe ordenar

	for j in range(1, len(B)):
		key = B[j]
		i = j - 1

		while i >= 0 and B[i] > key:
			B[i+1] = B[i]
			i = i - 1

		B[i+1] = key	

	A[p:f+1] = B  # Insertar subarreglo ordenado al arreglo original

# Merge Sort
def mergesort(T:[int]) -> "void":
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

def merge(U:[int], V:[int], T:[int]) -> "void":
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
def quicksortIterative(A:[int]) -> "void":
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
def quicksortSimple(A:[int], p:int, r:int) -> "void":
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

def partition(A:[int], p:int, r:int) -> int:
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
def medianOf3Quicksort(A:[int], f:int, b:int) -> "void":
	quicksortLoop(A, f, b)
	insertionsortIndex(A, f, b)
	# Debe llamarse la primera vez con:
	# MedianOf3Quicksort(A, 0, len(A))

def quicksortLoop(A:[int], f:int, b:int) -> "void":

	while b - f > 32:

		medianOf3 = statistics.median([A[f], A[f + (b-f)//2], A[b-1]])
		p = partitionMedianOf3(A, f, b, medianOf3)

		if (p - f) >= (b - p):
			quicksortLoop(A, p, b)
			b = p
		else:
			quicksortLoop(A, f, p)
			f = p

def partitionMedianOf3(A:[int], p:int, r:int, x:int) -> int:
	i = p - 1
	j = r
	while True:
		while True:
			j = j - 1
			if A[j] <= x:
				break
		while True:
			i = i + 1
			if A[i] >= x:
				break			
		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j

# Dual Pivot Quicksort
def dualPivotQuicksort(A:[int], left:int, right:int) -> "void":

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
