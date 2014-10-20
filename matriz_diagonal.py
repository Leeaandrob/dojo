class MatrizDiagonal(object):
    def __init__(self, i,j):
        self.i = i
        self.j = j
        self.matriz = self.cria_matriz_vazia()

    def get_matriz(self):
        return self.matriz

    def cria_matriz_vazia(self):
        matriz=[]
        for i in range(self.i):
            matriz.append([])
            for j in range(self.j):
                matriz[i].append(None)
        return matriz
    
    def set_diagonal(self):
        for i in range(self.i):
            self.matriz.append(0)
            for j in range(self.j):
                if self.i==self.j:
                    self.matriz[i].append[1]
            
            
