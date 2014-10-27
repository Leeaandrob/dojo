from unittest import TestCase
from minha_string import String

class StringTest(TestCase):
       
   def test_upper_case(self):
       
       esperado = "TESTE"
       objeto = String("teste")
       resposta = objeto.upper_case()

       self.assertEqual(resposta, esperado)
