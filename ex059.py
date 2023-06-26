num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
sair = False
while not sair:
    funcao = int(input(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos numeros \n [5] sair \n >>> Qual sua opção? '))
    if funcao == 1:
        soma = num1 + num2
        print('A soma dos numeros é {} !'.format(soma))
    elif funcao == 2:
        mult = num1 * num2
        print('A multiplicação dos numeros é {} !'.format(mult))
    elif funcao == 3:
        if num1 > num2:
            print('O maior numero entre os dois é {}'.format(num1))
        elif num1 == num2:
            print('Os dois numeros sao iguais')
        else:
            print('O maior numero entre os 2 é {}'.format(num2))
    elif funcao == 4:
        num1 = float(input('Digite novamente o primeiro valor: '))
        num2 = float(input('Agora digite o segundo valor: '))
    elif funcao == 5:
        sair = True
    else:
        print('Opcao invalida!! Digite uma opção valida \n <<<<<<<<<<>>>>>>>>>>')

print('Obrigado por usar nossos serviços! Volte sempre!!')
