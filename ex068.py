from random import randint
cont = 0
while True:
    comp = randint(0,10)
    jogador = str(input('Quer par ou impar? [P/I]').strip().upper()[0])
    valor = int(input('Digite o valor: [0 a 10 - voce só tem 10 dedos na mao]: '))
    soma = comp + valor
    resul = (comp + valor) % 2
    if resul == 1 and jogador == 'I':
        cont +=1
        print(f'Voce escolheu {valor} e eu {comp}. {soma} é Impar')
        print('Voce ganhou')
    elif resul == 0 and jogador == 'P':
        cont +=1
        print(f'Voce escolheu {valor} e eu {comp}. {soma} é Par')
        print(' Voce ganhou')
    elif resul == 0 and jogador == 'I':
        print(f'Voce escolheu {valor} e eu {comp}. {soma} é Par e voce infelimenste escolheu Impar')
        print('Voce perdeu!')
        break
    else:
        print(f'Voce escolheu {valor} e eu {comp}. {soma} é Impar e voce infelismente escolheu Par')
        print('Voce perdeu!')
        break

print(f'Voce ganhou {cont} seguidas!')

