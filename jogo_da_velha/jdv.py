def imprimir_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")


def verificar_vencedor(tabuleiro, jogador):
    
    combinacoes_vitoria = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]  
    ]
    for combinacao in combinacoes_vitoria:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False


def verificar_empate(tabuleiro):
    return all(celula != ' ' for celula in tabuleiro)


def jogar():
    
    tabuleiro = [' '] * 9
    jogador_atual = 'X'  

   
    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é sua vez!")

        
        try:
            jogada = int(input("Escolha uma posição de 1 a 9: ")) - 1
            if tabuleiro[jogada] != ' ':
                print("Posição ocupada! Escolha outra.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Escolha um número entre 1 e 9.")
            continue

        tabuleiro[jogada] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogar()
