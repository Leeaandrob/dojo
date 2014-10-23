from unittest import TestCase

from matriz_diagonal import MatrizDiagonal

class MatrizTest(TestCase):
    def test_get_matriz(self):
        esperado = [
            [None,None,None],
            [None,None,None],
            [None,None,None],
        ] 

        matriz = MatrizDiagonal(3,3)

        resposta = matriz.get_matriz()
        self.assertEqual(resposta, esperado)
    
    
    def test_matriz_vazia(self):
        esperado = [
            [None,None],
            [None,None]
        ]

        matriz = MatrizDiagonal(2,2)
        resposta = matriz.cria_matriz_vazia()
        self.assertEqual(resposta, esperado)
    
    
    def test_set_diagonal(self):        
        esperado = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            ]
        matriz = MatrizDiagonal(3,3)
        resposta = matriz.set_diagonal()
        self.assertEqual(resposta,esperado)
