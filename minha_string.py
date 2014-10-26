class MinhaString(object):
    def __init__(self, nome):
        self.nome = nome

    def NewString(self, meu_objeto):
        self.nome = meu_objeto
        return self.nome

    def upper_case(self):
        self.nome  = self.nome.upper()
        return self.nome
