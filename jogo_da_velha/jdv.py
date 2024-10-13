# Função para imprimir o tabuleiro do jogo
def imprimir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Todas as combinações possíveis para vencer
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combinacao in combinacoes_vitoria:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    return all(celula != ' ' for celula in tabuleiro)

# Função principal do jogo
def jogar():
    # Inicializar o tabuleiro vazio
    tabuleiro = [' '] * 9
    jogador_atual = 'X'  # X começa jogando

    # Loop principal do jogo
    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez!")

        # Solicitar a jogada do jogador
        try:
            jogada = int(input("Escolha uma posição de 1 a 9: ")) - 1
            if tabuleiro[jogada] != ' ':
                print("Posição ocupada! Escolha outra.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Escolha um número entre 1 e 9.")
            continue

        # Atualizar o tabuleiro com a jogada
        tabuleiro[jogada] = jogador_atual

        # Verificar se o jogador atual venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        # Verificar se o jogo terminou em empate
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alternar entre os jogadores
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Executar o jogo
jogar()
