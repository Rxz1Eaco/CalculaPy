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
    divisao = num1/num2
    print(f'A divisão entre número {num1} e o número {num2} é {divisao}')

def multiplicacao():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    multiplicacao = num1*num2
    print(f'A multiplicação entre número {num1} e o número {num2} é {multiplicacao}')

nome = str(input('Qual é o seu nome : '))
print(f'Seja bem-vindo {nome}')
print(f'{nome}, preciso que você escolha uma dessas operações: Soma, Subtração, Divisão, Multiplicação, Exponenciação')
op = str(input('Qual operação você deseja: '))


if op == 'Soma':
    soma()

elif op == 'Subtração':
    subtracao()

elif op == 'Divisão':
    divisao()


else:
    print('Operação Incorreta, tente novamente')