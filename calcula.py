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


def bhaskara():
    print("Você escolheu a opção Cálculo de Bhaskara/Função do 2° Grau")
    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    c = float(input("Digite o coeficiente 'c': "))
    delta = b**2 - 4 * a * c
    print(
        f"O coeficiente 'a' é {a}, coeficiente 'b' é {b} , coeficiente 'c' é {c} e o delta é {delta}"
    )
    if delta > 0:
        x1 = (-b + (delta**0.5)) / (2 * a)
        x2 = (-b - (delta**0.5)) / (2 * a)
        print(f"As raízes da equação são: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A equação possui uma raiz dupla: x = {x}")
    else:
        print("A equação não possui raízes reais.")


def raiz_quadrada():
    print("Você escolheu a opção da Raiz Quadrada")
    num_raiz = int(input("Digite o número para  calcularmos a raiz: "))
    raiz_quadrada = num_raiz**0.5
    print(f"A raiz quadrada {num_raiz} é {round(raiz_quadrada,2)}")


while True:
    print("|______________________|")
    print("|_______CalculaPy______|")
    print("|______________________|")

    nome = str(input("Qual é o seu nome ?\n"))
    print(f"Olá {nome}, eu sou o ChamaPy🤖.")
    idade = int(input(f"Qual é a sua idade, {nome}? \n"))

    ## Para Crianças: ##
    # idade >= 0 and idade <= 12
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
    # idade >= 13 AND idade <=100
    elif 13 <= idade <= 100:
        ## Para Adultos ##
        print(f"Seja Bem-Vindo: {nome} 🎉 ao CalculaPy")
        print(
            f"{nome}, você precisa selecionar uma das operações:\n"
            "Soma(+),\n"
            "Somando vários números(++),\n"
            "Subtração(-),\n"
            "Multiplicação(*),\n"
            "Divisão(/),\n"
            "Exponenciação(**),\n"
            "Função do 2° Grau(Delta)\n"
            "Raiz Quadrada(%)"
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
        elif op == "Função do 2° Grau" or op == "Delta":
            bhaskara()
        elif op == "Raiz Quadrada" or op == "%":
            raiz_quadrada()
        else:
            print("Opção Incorreta")
    else:
        print("Resposta inválida. Por favor, responda valores reais")
