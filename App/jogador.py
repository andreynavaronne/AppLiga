class Jogador:
    def __init__(self, nome:str, minutos:int, pontos:int):
        self.nome = nome
        self.pontos = pontos
        self.minutos = minutos
        self.media = pontos/(minutos/60)

    def calculaMedia(self):
        if self.minutos == 0:
            self.media = 0
        else:
            self.media = (self.pontos / self.minutos) * 60
    
    def aumentaPontos(self, pontos_jogo):
        self.pontos = self.pontos + pontos_jogo

    def aumentaMinutos(self, minutos_jogo):
        self.minutos = self.minutos + minutos_jogo
    
    def retornaHoras(self):
        horas = self.minutos // 60
        minuto = self.minutos % 60
        return f"{horas}:{minuto}"
    
    def getNome(self):
        return self.nome
    
    def getPontos(self):
        return self.pontos
    
    def getMedia(self):
        return self.media