def soma():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    soma = num1+num2
    print(f'A soma entre número {num1} e o número {num2} é {soma}')

def subtracao():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    subtracao = num1-num2
    print(f'A subtração entre número {num1} e o número {num2} é {subtracao}')

def divisao():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if num1 == 0 or num2 == 0:
        print(f'Qualquer número divido por 0 é igual a 0.')
    else:
        divisao = num1/num2
        print(f'A divisão entre número {num1} e o número {num2} é {divisao}')

def multiplicacao():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    multiplicacao = num1*num2
    if num1 == 0 or num2 == 0:
        print(f'Qualquer número multiplicado por 0 é igual a 0.')
    else:
        print(f'A multiplicação entre número {num1} e o número {num2} é {multiplicacao}')

def exponenciacao():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    exponencicao = num1**num2
    if num2 == 0:
        print('Qualquer número elevado a 0 é 1')
    else:
        print(f'A exponenciação entre número {num1} e o número {num2} é {exponencicao}')