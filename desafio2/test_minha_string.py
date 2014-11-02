from unittest import TestCase
from minha_string import String
from unittest import skipIf
class StringTest(TestCase):
       
   def test_upper_case(self):
       esperado = "LEANDRO"
       objeto = String("leandro")
       resposta = objeto.upper_case()

       self.assertEqual(resposta, esperado) 
  
   def test_upper_case_com_caracteres_especiais(self):
       esperado = "T4ST4 MINHA STRING_@12345"
       objeto = String("T4st4 minha string_@12345")
       resposta = objeto.upper_case()
       
       self.assertEqual(resposta, esperado)
        
   def test_tamanho(self): 
       esperado = 5
       objeto = String("Teste")
       resposta = objeto.tamanho()
       
       self.assertEqual(resposta, esperado)

   def test_lower_case(self):
       esperado = "teste"
       objeto = String("TESTE")
       resposta = objeto.lower_case()
       
       self.assertEqual(resposta, esperado)
       
   def test_centralizar(self):
        esperado = "aaaatesteaaaa"
        objeto = String("teste")
        resposta = objeto.centralizar(4, "a")
        
        self.assertEqual(resposta, esperado) 

   def test_contador(self):
        esperado = 1
        objeto = String("teste")
        resposta = objeto.contador("tes")      
