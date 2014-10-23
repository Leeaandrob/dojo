class Matriz(object):
	def __init__(self, i, j):
		self.i = i
		self.j = j
		self.matriz = self.cria_matriz()

	def cria_matriz(self):
		matriz = []
		for i in range(self.i):
			matriz.append([])
			for j in range(self.j):
				matriz[i].append(None)
		return matriz

	def set_diagonal(self):
		for i in range(self.i):
			for j in range(self.j):
				if self.i == self.j :
					self.matriz[i][i] = 1
		return self.matriz

uma = Matriz(3,3)
uma.cria_matriz # cria matriz vazia
uma.set_diagonal() # set 1 na diagonal
print uma.matriz
print uma.matriz[2][2] #[linha][coluna]


