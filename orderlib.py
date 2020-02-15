# Insertion Sort
def insertionSort(A:[int]) -> "void":
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

# Merge Sort
def mergeSort(T:[int]) -> "void":
	""" Algoritmo que divide un arreglo a la mitad para ordenarlo.
	En caso de llegar a un subarreglo con pocos elementos, se aplica
	insertion sort para ordenar ese sub arreglo"""

	if len(T) <= 32:
		insertionSort(T)

	else:
		U = T[0:len(T)//2]
		V = T[len(T)//2:len(T)]
		mergeSort(U)
		mergeSort(V)
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
def quickSortIterative(A:[int]) -> "void":
	"""Version iterativa del Quick Sort
	
	A: Arreglo a ordenar
	"""

	N = len(A)
	n, m = 0, 1
	while m < N:
		n,m = n + 1, m * 2
	x = [0 for i in range(0,n)]
	y = [0 for i in range(0,n)]
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
def quickSortSimple(A:[int], p:int, r:int) -> "void":
	""" Algoritmo que ordena un arreglo por medio de "pivotes"
	El ultimo elemento del arreglo a ordenar es usado como pivote"""

	tamanoSecuencia = r - p + 1

	if tamanoSecuencia <= 32 and p < r:	
		insertionSortIndex(A, p, r)


	elif tamanoSecuencia > 32 and p < r:
		q = partition(A, p, r)	
		quickSortSimple(A, p, q-1)
		quickSortSimple(A, q+1, r)

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

def insertionSortIndex(A:[int], p:int, f:int) -> "void":
	"""Version modificada de Insertion Sort la cual solo ordena
	el subarreglo de A que inicie en la posicion p y termine en
	la posicion f. Luego, se inserta el subarreglo ordenado en 
	el arreglo original

	Es usado en el algoritmo Quick Sort Simple

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

