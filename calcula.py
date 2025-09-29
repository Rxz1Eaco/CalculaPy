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
        print('Qual número elevado a 0 é 1')
    elif num1 == 1:
        print('Qualquer número elevado a 1 é 0')
    else:
        print(f'A exponenciação entre número {num1} e o número {num2} é {exponencicao}')

nome = str(input('Qual é o seu nome : '))
print(f'Seja bem-vindo {nome}')
print(f'{nome}, preciso que você escolha uma dessas operações: Soma, Subtração, Divisão, Multiplicação, Exponenciação')
op = str(input('Qual operação você deseja: ')).lower()
if op == 'soma' :
    soma()

elif op == 'subtração':
    subtracao()

elif op == 'divisão':
    divisao()

elif op == 'multiplicação':
    multiplicacao()

elif op == 'exponenciação':
    exponenciacao()

else:
    print('Operação Incorreta, tente novamente')