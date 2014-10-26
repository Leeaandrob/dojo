from unittest import TestCase
from minha_string import MinhaString

class StringTest(TestCase):
   
   def test_NewString(self):
       
       esperado = "Teste"
       objeto = MinhaString(None)
       resposta = objeto.NewString("Teste")

       self.assertEqual(resposta, esperado)
       
       
   def test_upper_case(self):
       
       esperado = "TESTE"
       objeto = MinhaString("Teste")
       resposta = objeto.upper_case()

       self.assertEqual(resposta, esperado)
