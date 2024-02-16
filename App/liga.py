import jogador
import jogo

class Liga:
    def __init__ (self, edicao : int):
        self.edicao = edicao
        self.jogadores = []
        self.n_jogadores = len(self.jogadores)
        
    def adicionaJogador(self, Jogador):
        self.jogadores.append(Jogador)

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