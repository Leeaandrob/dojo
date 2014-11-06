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
        objeto = String("teste")
        self.assertEqual(objeto.tamanho(objeto), 5)
   
   def test_tamanho_com_string_vazia(self):
        objeto = String(" ")
        self.assertEqual(objeto.tamanho(objeto), 1)
   
   def test_tamanho_com_string_zero(self):
        objeto = String("")
        self.assertEqual(objeto.tamanho(objeto), 0)

   def test_lower_case(self):
       esperado = "teste"
       objeto = String("TESTE")
       resposta = objeto.lower_case()
       
       self.assertEqual(resposta, esperado)
   
   def test_lower_case_com_caracteres_especiais(self):
       esperado = "t4st4 @123456"
       objeto = String("T4sT4 @123456")
       resposta = objeto.lower_case()

       self.assertEqual(resposta, esperado)
       
   def test_centralizar(self):
        esperado = "teste"
        objeto = String("teste")
        resposta = objeto.centralizar(4, "a")
        
        self.assertEqual(resposta, esperado)
   
   def test_centralizar_com_largura_maior_que_tamanho(self):
       esperado = "testea"
       objeto = String("teste")
       resposta = objeto.centralizar(6, "a")
       
       self.assertEqual(resposta, esperado)
             
   def test_centralizar_com_largura_espaco_vazio(self):
       esperado = "teste "
       objeto = String("teste")
       resposta = objeto.centralizar(6)

       self.assertEqual(resposta, esperado)
   
