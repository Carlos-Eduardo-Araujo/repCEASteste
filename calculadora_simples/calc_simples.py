# Função para somar dois números
def somar(x, y):
    return x + y


# Função para subtrair dois números
def subtrair(x, y):
    return x - y


# Função para multiplicar dois números
def multiplicar(x, y):
    return x * y


# Função para dividir dois números
def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."


# Função principal
def calculadora():
    print("Selecione a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    # Recebe a escolha do usuário
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    # Recebe os números para a operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação escolhida
    if escolha == '1':
        print(f"{num1} + {num2} = {somar(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opção inválida")


# Executa a calculadora
calculadora()
