from opTutorial import (
    Somatutorial,
    SubTutorial,
    MultiTutorial,
    DivTutorial,
    ExpTutorial,
)


def soma():
    print("Você, escolheu a opção Soma")
    num1 = float(input(f"{nome}, digite o 1° número para somar: "))
    num2 = float(input(f"{nome}, agora digite o 2° número para somar: "))
    print(f"A soma entre o 1° número {num1} e 2° número {num2} = {num1+num2}")


def soma_varios_numeros():
    print("Você escolheu a opção Soma de vários números")
    entrada = input("Insira vários números separados por espaços: ")
    numeros_str = entrada.split()
    numeros = [float(num) for num in numeros_str]
    resultado = sum(numeros)
    print(f"A soma dos números é: {resultado}")


def subtracao():
    print("Você, escolheu a opção Subtração")
    num1 = float(input(f"{nome}, digite o 1° número para subtrair: "))
    num2 = float(input(f"{nome}, agora digite o 2° número para subtrair: "))
    print(f"A subtração entre o 1° número {num1} e 2° número {num2} = {num1-num2}")


def multiplicacao():
    print("Você, escolheu a opção Multiplicação ")
    num1 = float(input(f"{nome}, digite o 1° número para multiplicar: "))
    num2 = float(input(f"{nome}, agora digite o 2° número para multiplicar: "))
    print(f"A subtração entre o 1° número {num1} e 2° número {num2} = {num1*num2}")


def divisao():
    print("Você, escolheu a opção Divisão")
    num1 = float(input(f"{nome}, digite o 1° número para dividir: "))
    num2 = float(input(f"{nome}, agora digite o 2° número para dividir: "))
    print(f"A dvisão entre o 1° número {num1} e 2° número {num2} = {num1/num2}")


def exponenciacao():
    print("Você escolheu a opção Exponenciação")
    num1 = float(input(f"{nome}, digite o 1° número para exponenciar: "))
    num2 = float(input(f"{nome}, agora digite o 2° número para  exponenciar: "))
    print(f"A expoenciação entre o 1° número {num1} e 2° número {num2} = {num1**num2}")


while True:
    print("|______________________|")
    print("|_______CalculaPy______|")
    print("|______________________|")

    nome = str(input("Qual é o seu nome ?\n"))
    print(f"Olá {nome}, eu sou o ChamaPy🤖.")
    idade = int(input(f"Qual é a sua idade, {nome}? \n"))

    ## Para Crianças: ##
    # idade >= 1 and idade <= 10
    if 0 <= idade <= 12:
        op_tutorial = str(input("Você quer passar pelo Tutorial?\n" "Sim | Não\n"))
        if op_tutorial == "Sim" or op_tutorial == "sim":
            Somatutorial()
            SubTutorial()
            MultiTutorial()
            DivTutorial()
            ExpTutorial()
            print("Você já passou pelo nosso tutorial, Parabéns 🥳")
            print(f"Vamos por a mão na massa,{nome}?!")
            print(f"Seja Bem-Vindo: {nome} 🎉 ao CalculaPy")
            print(
                f"{nome}, você precisa selecionar uma das operações:\n"
                "Soma(+),\n"
                "Somando vários números(++)"
                "Subtração(-),\n"
                "Multiplicação(*),\n"
                "Divisão(/),\n"
                "Exponenciação(**),\n"
                "Sair"
            )
            op = str(input("Digite a operação que você escolheu: "))
            if op == "Soma" or op == "+":
                soma()
            elif op == "Somando vários números" or op == "++":
                soma_varios_numeros()
            elif op == "Subtração" or op == "-":
                subtracao()
            elif op == "Multiplicação" or op == "*":
                multiplicacao()
            elif op == "Divisão" or op == "/":
                divisao()
            elif op == "Exponenciação" or op == "**":
                exponenciacao()
            elif op == "Sair" or op == "sair":
                break
            else:
                print("Opção Incorreta")
        else:
            ## Crianças que falaram não ##
            print("Você, escolheu a opção de não passar pelo tutorial ")
            print(f"Vamos por a mão na massa,{nome}?!")
            print(f"Seja Bem-Vindo: {nome} 🎉 ao CalculaPy")
            print(
                f"{nome}, você precisa selecionar uma das operações:\n"
                "Soma(+),\n"
                "Somando vários números(++),\n"
                "Subtração(-),\n"
                "Multiplicação(*),\n"
                "Divisão(/),\n"
                "Exponenciação(**)\n"
                "Sair"
            )
            op = str(input("Digite a operação que você escolheu: "))
            if op == "Soma" or op == "+":
                soma()
            elif op == "Somando vários números" or op == "++":
                soma_varios_numeros()
            elif op == "Subtração" or op == "-":
                subtracao()
            elif op == "Multiplicação" or op == "*":
                multiplicacao()
            elif op == "Divisão" or op == "/":
                divisao()
            elif op == "Exponenciação" or op == "**":
                exponenciacao()
            elif op == "Sair" or op == "sair":
                break
            else:
                print("Opção Incorreta")
    elif idade >= 13:
        ## Para Adultos ##
        print(f"Seja Bem-Vindo: {nome} 🎉 ao CalculaPy")
        print(
            f"{nome}, você precisa selecionar uma das operações:\n"
            "Soma(+),\n"
            "Somando vários números(++),\n"
            "Subtração(-),\n"
            "Multiplicação(*),\n"
            "Divisão(/),\n"
            "Exponenciação(**)"
        )
        op = str(input("Digite a operação que você escolheu: "))
        if op == "Soma" or op == "+":
            soma()
        elif op == "Somando vários números" or op == "++":
            soma_varios_numeros()
        elif op == "Subtração" or op == "-":
            subtracao()
        elif op == "Multiplicação" or op == "*":
            multiplicacao()
        elif op == "Divisão" or op == "/":
            divisao()
        elif op == "Exponenciação" or op == "**":
            exponenciacao()
        else:
            print("Opção Incorreta")

    else:
        print("Resposta inválida. Por favor, responda valores reais")
