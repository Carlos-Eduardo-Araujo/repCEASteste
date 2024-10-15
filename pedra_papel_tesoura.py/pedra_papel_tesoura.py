import random

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'tesoura' and computador == 'papel') or \
            (jogador == 'papel' and computador == 'pedra'):
        return "Você venceu!"
    else:
        return "Você perdeu!"

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in opcoes:
        print("Escolha inválida!")
        return

    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    resultado = determinar_vencedor(jogador, computador)
    print(resultado)


jogar()
