import jogador
import jogo

class Liga:
    def __init__ (self, edicao : int , n_jog : int):
        self.edicao = edicao
        self.n_jog = n_jog
        self.jogadores = [jogador.Jogador(None)] * n_jog
        self.posicao = 0

    def adicionaJogador(self, Jogador):
        if self.n_jog > self.posicao:
              self.jogadores[self.posicao] = jogador
              self.posicao += 1

    def buscaJogador(self, jogador : str):
        busca = 0
        retorno = None
        while busca < self.n_jog:
          nome_busca = self.jogadores[busca].getNome()
          if nome_busca == jogador:
               retorno = self.jogadores[busca]
        return retorno
    
    def existeJogador(self, jogador : str):
        busca = 0
        while busca < self.n_jog:
            nome_busca = self.jogadores[busca].getNome()
            if nome_busca == jogador:
                return True
        return False