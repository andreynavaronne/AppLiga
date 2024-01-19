from openpyxl import Workbook
from openpyxl import load_workbook
import jogador
import jogo
import liga

n = 0

arquivo = open("AppLiga/App/info.txt", "r")
lines = arquivo.readlines()
splitar = lines[0].split(" ")
n_liga = splitar[1]

while n != 4:
    print("Bem-vindo ao AppLiga!\nO que você gostaria de fazer?\n\n (1) Atualizar Liga Atual\n (2) Terminar Liga\n (3) Começar nova liga\n (4) Sair")
    escolha = int(input())
    if escolha == 1:
        tabela_nome = "liga" + n_liga
        tabela = load_workbook(tabela_nome)
        tb = tabela.active
        a = 0
        while a != 5:
            print(" (1) Adicionar Novo Jogo\n (2) Apagar Jogo\n (3) Ver Tabela \n (4) Adicionar jogador tardío\n (5) Sair")
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