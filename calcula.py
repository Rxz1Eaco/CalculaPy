from operacao import soma, subtracao, divisao, multiplicacao, exponenciacao

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