# NumPy é uma biblioteca matemática
import numpy as py  # importamos numpy como "py"

# Listas são mutáveis e compatíveis com NumPy (desde que bem formatadas)
y = [[0, 1], [1, 2], [3, 4]]
print("Lista original (y):")
print(y)
print("Tipo de y:", type(y))

# Conversão para array NumPy
yarray = py.array(y)
print("\nArray NumPy (yarray):")
print(yarray)
print("Tipo:", type(yarray))
print("Shape (formato):", yarray.shape)
print("Dtype (tipo de dado):", yarray.dtype)

# Multiplicação elemento a elemento
print("\nMultiplicação elemento a elemento:")
muly = yarray * yarray
print(muly)

# Multiplicação matricial (produto de matriz)
print("\nMultiplicação matricial (yarray @ yarray.T):")
muly2 = yarray @ yarray.T
print(muly2)

# Transposta da matriz
print("\nMatriz transposta (yarray.T):")
print(yarray.T)

# Produto interno entre vetores
a = py.array([1, 2, 3])
b = py.array([4, 5, 6])
print("\nProduto interno entre vetores a e b:")
print("a =", a)
print("b =", b)
print("inner(a, b):", py.inner(a, b))

# Produto interno entre matrizes (produto entre linhas)
a = py.array([[1, 2], [3, 4]])
b = py.array([[5, 6], [7, 8]])
print("\nProduto interno entre matrizes a e b (linha por linha):")
print("a =\n", a)
print("b =\n", b)
print("inner(a, b):\n", py.inner(a, b))
#tensorflow: é uma biblioteca de código aberto desenvolvida pelo Google ,
# TensorFlow é um sistema que manipula tensores através de uma sequência de operações matemáticas.
#Tensor = estrutura de dados multidimensional 
#sistema AI  