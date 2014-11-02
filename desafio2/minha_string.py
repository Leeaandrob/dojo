class String(object):
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.maisculo = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","Z"]
        self.minusculo = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","x","z"]
    
    def indice(self, letra, lista):
        indice=0
        if not letra in lista:
            return -1
        for l in lista:
            if l == letra:
                return indice
            else:
                indice+=1

    def upper_case(self): 
        saida =  ""
        for letra in self.conteudo:
            indice = self.indice(letra, self.minusculo)
            if indice != -1:
                saida+=self.maisculo[indice]
            else:
                saida+=letra
        return saida

    def lower_case(self):
        saida = ""
        for letra in self.conteudo:
            indice = self.indice(letra, self.maisculo)
            if indice != -1:
                saida+=self.minusculo[indice]
            else:
                saida+=letra
        return saida

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
        if count in self.conteudo:
            numero+=1
        return numero
    
    def slice(self, comeco, fim, reposta):
        if comeco > self.conteudo or self.conteudo > fim:
            reposta = False
        else:
            resposta = True
        letras = self.conteudo
        comeco = letras[comeco:]
        final  = letras[:final]
        return True  
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
