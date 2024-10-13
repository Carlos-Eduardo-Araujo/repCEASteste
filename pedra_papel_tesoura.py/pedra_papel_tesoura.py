import random


# Função para determinar o vencedor
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'tesoura' and computador == 'papel') or \
            (jogador == 'papel' and computador == 'pedra'):
        return "Você venceu!"
    else:
        return "Você perdeu!"


# Função principal do jogo
def jogar():
    # Opções possíveis
    opcoes = ['pedra', 'papel', 'tesoura']

    # Solicitar a escolha do jogador
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    # Validar a escolha do jogador
    if jogador not in opcoes:
        print("Escolha inválida!")
        return

    # Escolha do computador
    computador = random.choice(opcoes)

    # Exibir as escolhas
    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    # Determinar e exibir o resultado
    resultado = determinar_vencedor(jogador, computador)
    print(resultado)


# Executa o jogo
jogar()