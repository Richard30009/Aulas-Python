primeiro = int(input('Digite o Termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='' )
    termo += razao
    cont += 1
print('FIM - Esses sao os 10 primeiros termos!')
