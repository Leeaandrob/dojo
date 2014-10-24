class MatrizDiagonal(object):
    def __init__(self, i,j, conteudo):
        
        if i != j :
            raise Exception('Apenas raiz quadrada')

        self.i = i
        self.j = j
        self.conteudo = conteudo
        self.matriz = self.cria_matriz_vazia()

    def get_matriz(self):
        return self.matriz

    def cria_matriz_vazia(self):
        return [[self.conteudo for j in range(self.j)]
            for i in range(self.i)]
        
         
    def set_diagonal(self):
        for i in range(self.i):
                    self.matriz[i][i] = 1
        return self.matriz
            
            
