import jogador
import jogo
import liga
import math

n = 0

arquivo = open("AppLiga/App/info.txt", "r")
lines = arquivo.readlines()
splitar = lines[0].split(" ")
n_liga = splitar[1]
arquivo.close()

while n != 4:
    print("Bem-vindo ao AppLiga!\nO que você gostaria de fazer?\n\n (1) Atualizar Liga Atual\n (2) Terminar Liga\n (3) Começar nova liga\n (4) Sair")
    escolha = int(input())
    if escolha == 1:
        nome_liga = f"{splitar[0]}{splitar[1]}"
        liga_arq = open(f"AppLiga/App/{nome_liga}/liga", "r")
        a = 0
        lista = liga.readlines()
        ligaAtual = liga.Liga(n_liga)
        if len(lista) <= 0:
            print("Liga não possui jogadores. Algum erro aconteceu.")
        else:
            lista_jogs = []
            t_jogs = len(lista)
            for i in range(t_jogs):
                split = lista[i].split(" ")
                nome_jog = split[0]
                minutos_jog = split[1]
                pontos_jog = split [2]
                novo_jog = jogador.Jogador(nome_jog, minutos_jog, pontos_jog)
                ligaAtual.adicionaJogador(novo_jog)
        liga.close()
        while a != 5:
            print(" (1) Adicionar Novo Jogo\n (2) Apagar Jogo\n (3) Ver Tabela \n (4) Adicionar jogador tardío\n (5) Sair")
            if a == 1:
                nome_jogo = input("Digite o nome do jogo:\n")
                tempo_caixa_jogo = int(input("Digite o tempo de caixa do jogo (em minutos):\n"))
                tempo_real_jogo = int(input("Digite o tempo que durou o jogo (em minutos):\n"))
                tempo_media = ((tempo_caixa_jogo + tempo_real_jogo)//2)
                tempo_procura = math.ceil(tempo_media/5)*5
                qnt_jogadores = int(input("Digite quantos jogadores jogaram:\n"))
                qnt_procura = 0
                if qnt_jogadores > 5:
                    qnt_procura = 5
                else:
                    qnt_procura = qnt_jogadores
                pontuacoes = open(f"AppLiga/Pontuações/{qnt_procura}jogs.txt", "r")
                valores = []
                linhas = pontuacoes.readlines()
                for j in range(len(linhas)):
                    splits = linhas.split("")
                    if splits[0] == tempo_procura:
                        for k in range(qnt_procura):
                            valores.append(splits[k+1])
                jogadores_arquivo = open(f"AppLiga/App/{nome_liga}/liga.txt", "r")
                liga_jogs = jogadores_arquivo.readlines()
                jogadores = []
                jogadores_arquivo.close()
                for a in range(len(liga_jogs)):
                    player = liga_jogs[a].split(" ")[0]
                    jogadores.append(player)
                ordem_jogo = []
                for i in range(qnt_jogadores):
                    novo_jog = input(f"Digite o jogador que ficou na {i+1}ª posição:\n")
                    ordem_jogo.append(novo_jog)
                    if not(ligaAtual.buscaJogador(novo_jog)):
                        erroJog = input(print(f"Jogador {novo_jog} não existente na liga. Adicionar nos convidados (tecle 1) ou alterar nome? (tecle 2)\n"))
                        if erroJog == "1":
                                convidados_arq = open(f"AppLiga/App/{nome_liga}/convidados.txt", "a")

                pontuacoes = open(f"AppLiga/Pontuações/{qnt_procura}jogs.txt", "r")
                valores = []
                linhas = pontuacoes.readlines()
                for j in range(len(linhas)):
                    splits = linhas.split("")
                    if splits[0] == tempo_procura:
                        for k in range(qnt_procura):
                            valores.append(splits[k+1])
                
                print("Jogo adicionado")                    
    elif escolha == 2:
        print(f"Você realmente deseja terminar a Liga {n_liga}ª Edição? sim/não")
        resposta = input()
        if resposta == "não":
            print("Retornando para o menu de atualização")
        elif resposta == "sim":
            print("Digite 'terminar' para confirmar")
            confirmacao = input()
            if confirmacao == "terminar":
                print("Iniciando processo de fim de liga...")
            else:
                print("Retornando para o menu de atualização")
        else:
            print("Opção inválida, retornando para o menu de atualização")
    elif escolha == 3:
        print("Você deseja iniciar uma nova liga? sim/não")
        resp = input()
        if resp == "sim":
            arquivo2 = open("AppLiga/App/info.txt", "w")
            n_novo = n_liga + 1
            arquivo2.write(f"liga_atual {n_novo}")
            print(f"Liga {n_novo}ª Edição pronta para ser inicializada\nQuantos jogadores participarão?")
            try:
                 n_jog = int(input())
            except ValueError:
                print("Valor inválido, insira um número inteiro")
            finally:
                posicao = 1
                nova_liga = liga.Liga(n_novo, n_jog)
                while n_jog > 0:
                    print(f"Digite o nome do {posicao}º jogador")
                    nome = input()
                    jogador = jogo.Jogador(nome)
                    nova_liga.adicionaJogador(jogador)
                    posicao += 1
                    n_jog -= 1
    elif escolha == 4:
        n = 4