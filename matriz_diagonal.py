class MatrizDiagonal(object):
    def __init__(self, i,j, conteudo):
        self.i = i
        self.j = j
        self.conteudo = conteudo
        self.matriz = self.cria_matriz_vazia()

    def get_matriz(self):
        self.conteudo = 0
        return self.matriz

    def cria_matriz_vazia(self):
        matriz=[]
        for i in range(self.i):
            matriz.append([])
            for j in range(self.j):
                matriz[i].append(self.conteudo)
        return matriz
    
    def set_diagonal(self):
        for i in range(self.i):
            for j in range(self.j):
                if i==j:
                    self.matriz[i][j] = 1
        return self.matriz
            
            
