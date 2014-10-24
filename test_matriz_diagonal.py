from mock import patch
from unittest import TestCase
from matriz_diagonal import MatrizDiagonal

class MatrizTest(TestCase):

    @patch('matriz_diagonal.MatrizDiagonal.cria_matriz_vazia')

    def test_instance(self, _method):
        _method.return_value = 'foo'
        obj = MatrizDiagonal(3,3,0)
        self.assertEqual(obj.i, 3)
        self.assertEqual(obj.j, 3)
        self.assertEqual(obj.matriz, 'foo')

    def test_apenas_matriz_quadrada(self):
        with self.assertRaisesRegexp(Exception, 'apenas raiz quadrada'):
            obj = MatrizDiagonal(2,3,0)

    def test_get_matriz(self):
        esperado = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ] 

        matriz = MatrizDiagonal(3,3,0)

        resposta = matriz.get_matriz()
        self.assertEqual(resposta, esperado)
    
    
    def test_matriz_vazia(self):
        esperado = [
            [0,0],
            [0,0]
        ]

        matriz = MatrizDiagonal(2,2,0)
        resposta = matriz.cria_matriz_vazia()
        self.assertEqual(resposta, esperado)
    
    
    def test_set_diagonal(self):        
        esperado = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            ]
        matriz = MatrizDiagonal(3,3,0)
        resposta = matriz.set_diagonal()
        self.assertEqual(resposta,esperado)
