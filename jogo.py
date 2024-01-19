class Jogo:
    def __init__(self, nome, d_caixa, d_real, jogadores):
        self.nome = nome
        self.d_caixa = d_caixa
        self.d_real = d_real
        self.jogadores = jogadores

    def multiplicadores(self):
        pontos = ""
        if self.jogadores < 6:
            pontos = f"{self.jogadores}jogs.txt"
        else:
            pontos = "5jogs.txt"
        arquivo = open(f"Pontuações/{pontos}", "r")
        linhas = arquivo.readlines()
        linha = (self.d_caixa + self.d_real) // 5
        pontuacoes = linhas[linha].split(" ")
        pontuacoes.remove(pontuacoes[0])
        return pontuacoes
