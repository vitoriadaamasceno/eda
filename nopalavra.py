class NoPalavra:
    def __init__(self, palavra):
        self.ocorrs = 0
        self.proxPalavra = None
        self.linhas = None
        self.proxTamanho = None
        self.palavra = palavra
    
    def get_palavra(self):
        return self.palavra
    
    def set_palavra(self,palavra):
        self.palavra = palavra

    def get_proxPalavra(self):
        return self.proxPalavra
    
    def set_proxPalavra(self,proximo):
        self.proxPalavra = proximo

