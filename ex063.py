soma = 0
cont = 0
num = int(input('Digite um valor [999 para sair]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um valor [999 para sair]: '))

print('voce digitou {} vezes e a soma dos valores é {}'.format(cont, soma))