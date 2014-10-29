from unittest import TestCase
from minha_string import String

class StringTest(TestCase):
       
   def test_upper_case(self):
       
       esperado = "LEANDRO"
       objeto = String("leandro")
       resposta = objeto.upper_case()

       self.assertEqual(resposta, esperado)

   def test_tamanho(self):
       
       esperado = 5
       objeto = String("Teste")
       resposta = objeto.tamanho()
       
       self.assertEqual(resposta, esperado)
