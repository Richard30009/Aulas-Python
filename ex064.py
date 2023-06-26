
num = int(input('Digite um numero: '))
sair = str(input('Deseja continuar [S/N]: ').strip().upper()[0])
cont = 1
soma = num
menor = num
maior = num

while sair not in 'N':
    cont += 1
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    elif num < menor :
        menor = num
    soma = soma + num
    sair = str(input('Deseja continuar [S/N]: ').strip().upper()[0])

media = soma / cont
print('Voce digitou {} e a media dos numero é {} '.format(cont, media))
print(' O menor sumero foi {} e o maior {}'.format(menor,maior))
