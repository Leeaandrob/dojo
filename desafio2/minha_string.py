class String(object):
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.maisculo = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z"]
        self.minusculo = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"]

    def upper_case(self):
        letras = ""
        contador = 0
        for i in self.conteudo:
            for j in self.minusculo:
                if i != j :
                    contador+=1
                else:
                    letras+=self.maisculo[contador]
            contador=0
            self.conteudo = letras
        return self.conteudo

    def lower_case(self):
        letras = ""
        contador = 0 
        for i in self.conteudo:
            for j in self.maisculo:
                if i != j:
                    contador+=1
                else:
                    letras+=self.minusculo[contador]
            contador = 0
            self.conteudo = letras
        return self.conteudo
                
    def tamanho(self):
        tamanho = 0 
        for i in self.conteudo:
            tamanho +=1
        return tamanho
   
    def centralizar(self, largura, letra):
        width = (largura*letra)+self.conteudo+(largura*letra)
        return width
         
    def contador(self, count):
        numero = 0
        for i in self.conteudo:
            if count in self.conteudo:
                numero+=1
        return numero
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
